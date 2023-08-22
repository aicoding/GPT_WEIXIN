import os
import chainlit as cl
from language.gettext import get_text
import webbrowser

async def need_file_upload():
    """
    Unless the user actively requests to upload and includes the words 'upload file' or 'upload image' in their input, do not invoke this function.
    Parameters: None
    """
    if not os.path.exists('./tmp'):
        os.mkdir('./tmp')
    files = await cl.AskFileMessage(
        content="Please upload a file.",
        max_size_mb=10,
        accept=[
            "*"
        ]).send()
    file = files[0]
    save_path = ""
    # 保存文件到paths目录下
    # 判断paths目录是否存在
    if save_path == "":
        save_path = file.name
    file_path = f"./tmp/{save_path}"
    # 保存文件
    content = file.content
    # 保存文件
    # content是bytes类型
    with open(file_path, "wb") as f:
        f.write(content)
    message_history = cl.user_session.get("message_history")
    message_history.append({
        "role": "assistant",
        "content": f"upload file ./tmp/{save_path} success"
    })
    await cl.Message(
        author="Chatbot",
        content=f"{get_text(os.environ.get('LANGUAGE') or 'chinese', 'upload_notification')} ./tmp/{save_path}",
    ).send()
    return {
        'description': f"upload file ./tmp/{save_path} success",
    }
    
async def need_rename_file(old_path: str, new_path: str):
    """
    When the user's question refers to managing files and requires file rename, you can invoke this function.
    Parameters: old_path: The old path of the file.(required)
    new_path: The new path of the file.(required)
    """
    # 判断old_path是否存在
    if not os.path.exists(old_path):
        return {'description': f"{old_path} is not exist"}
    # 判断new_path是否存在
    if os.path.exists(new_path):
        os.remove(new_path)
    # 重命名文件
    os.rename(old_path, new_path)
    return {'description': f"rename file {old_path} to {new_path} success"}

# 使用webbrowser打开HTML文件
async def open_file_with_webbrowser(file_path:str):
    """
    用浏览器打开这个文件的地址.
    Parameters:
        file_path: The file_path statement.(required)
    """
    webbrowser.open(file_path)    