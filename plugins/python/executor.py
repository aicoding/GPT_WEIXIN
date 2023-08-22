import asyncio
import base64
from concurrent.futures import ThreadPoolExecutor
import time
from jupyter_client.manager import KernelManager
from queue import Empty
import re
from PIL import Image
import io

# 定义移除ANSI转义序列的函数
def remove_ansi_escape_sequences(s):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', s)


class CodeExecutor:
    def __init__(self):
        self.km = None
        self.kc = None
        self.executor = None
        self.timeout_task = None

    async def start_kernel(self):
        if self.km is None or self.kc is None or self.executor is None:
            self.km = KernelManager()
            self.km.start_kernel()
            self.kc = self.km.blocking_client()
            self.kc.start_channels()
            self.executor = ThreadPoolExecutor(max_workers=1)
            self.timeout_task = asyncio.create_task(self.auto_shutdown())

    async def auto_shutdown(self):
        await asyncio.sleep(180)  # 15 minutes
        self.shutdown()

    async def execute(self, code):
        if self.timeout_task is not None:
            self.timeout_task.cancel()
        await self.start_kernel()
        # 执行代码
        msg_id = self.kc.execute(code)

        # 用于保存所有收到的消息
        all_msgs = []

        # 等待执行结果
        while True:
            try:
                # 在新的线程中运行 get_iopub_msg 方法，并在异步函数中等待它的完成
                msg = await asyncio.get_event_loop().run_in_executor(self.executor, self.kc.get_iopub_msg, 60)
            except Empty:
                return None
            else:
                if msg["parent_header"].get("msg_id") == msg_id:
                    msg_type = msg["msg_type"]
                    content = msg["content"]
                    print(f"msg_type: {msg_type}, content: {content}")
                    if msg_type == "execute_result" or msg_type == "display_data":
                        if "image/png" in content["data"]:
                            # 正则表达式，用于匹配以 .gif 结尾的字符串
                            gif_pattern = r"'(.*\.gif)'"

                            # 使用正则表达式匹配代码中的 .gif 文件名
                            gif_filenames = re.findall(gif_pattern, code)
                            if len(gif_filenames) > 0:
                                for filename in gif_filenames:
                                    all_msgs.append(f'show image: {filename}')
                            else:
                                # 存成文件
                                file_path = f'./tmp/{time.time()}.png'
                                image_data = base64.b64decode(content['data']["image/png"])
                                image = Image.open(io.BytesIO(image_data))
                                image.save(file_path)
                                all_msgs.append(f'show image: {file_path}')
                        else:
                            all_msgs.append(content["data"]["text/plain"])
                    elif msg_type == "stream":
                        all_msgs.append(content["text"])
                    elif msg_type == "error":
                        # 提取错误信息
                        traceback = content['traceback']
                        user_traceback = [remove_ansi_escape_sequences(line) for line in traceback]
                        # 我需要取0,1和-1行
                        indices_to_try = [2, 3, -1]  # Indices we are interested in
                        final_error = []

                        if len(user_traceback) >= 4:
                            for index in indices_to_try:
                                element = str(user_traceback[index])
                                if element not in final_error:  # Check for duplicates
                                    final_error.append(element)
                        else:  
                            # Keep all elements for lengths less than 4
                            final_error = [str(item) for item in user_traceback]
                        error_info = '\n'.join(final_error)
                        return f"Error info:\n{error_info}"
                    elif msg_type == "status" and content['execution_state'] == 'idle':
                        # 只保留all_msgs中的最后三个元素,不足三个元素则全部保留
                        if len(all_msgs) > 3:
                            all_msgs = all_msgs[-3:]
                        return '\n'.join(all_msgs)
        self.timeout_task = asyncio.create_task(self.auto_shutdown())
                   
    def shutdown(self):
        if self.km is not None and self.kc is not None and self.executor is not None:
            time.sleep(2)
            self.kc.stop_channels()
            self.km.shutdown_kernel()
            self.executor.shutdown()
            self.km = None
            self.kc = None
            self.executor = None
            self.timeout_task = None


async def main():
    executor = CodeExecutor()
    res = await executor.execute("""import matplotlib.pyplot as plt
import numpy as np

# Generate 10 random numbers
random_numbers = np.random.rand(10)

# Plot the random numbers
plt.plot(random_numbers)

# Display the plot
plt.show()                          
    """)
    print("====================================")
    print(res)
    print("====================================")
    executor.shutdown()

if __name__ == "__main__":
    asyncio.run(main())
    # from PIL import Image, ImageFilter
    # # Open an image file
    # img = Image.open('../../tmp/1.png')
    # # Apply a blur filter to the image
    # blurred = img.filter(ImageFilter.BLUR)
    # # Save the blurred image
    # blurred.save('./tmp/blurred.png')
    # print('path', './tmp/blurred.png')
