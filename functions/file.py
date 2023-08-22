import json
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Line
import matplotlib.pyplot as plt

base_url = "http://localhost:8000/tmp/"

def write_file(save_path:str,data: str):
    """
    If the user's question mentions the need to write file, you can call this function.
    Parameters:
        data: The data statement.(required)
    """
    save_path = "metric.txt"
    # 保存文件到paths目录下
    # 判断paths目录是否存在
    if save_path == "":
        save_path = file.name
    file_path = f"./tmp/{save_path}"
    # 打开文件以进行写入（如果文件不存在会创建文件，如果文件已存在会清空文件内容）
    with open(file_path, "w") as file:
        file.write(data)
    # 文件会在退出with块时自动关闭
    print("文件写入完成")
    return base_url + file_path


#请求指标返回today,dod,wow数据生成echarts图表    
def generate_charts_file(data: str):
    """
    If the user's question mentions the need to generate charts, you can call this function.
    Parameters:
        data: The data statement.(required)
    """
    if data == '' or data is None :
        return {"status": "false", "error": 'Data error, can not generate the chart'}
    # 将数据转换成DataFrame格式
    if(type(data) is str):
        df = pd.DataFrame(json.loads(data)) 
    else:
        df = pd.DataFrame(data)
    # 创建Line实例
    line = Line()
    # 添加x轴数据，即日期
    line.add_xaxis(df["x"].tolist())

    # 添加y轴数据，即各个系列的数据
    line.add_yaxis("today", df["today"].tolist())
    line.add_yaxis("dod", df["dod"].tolist())
    line.add_yaxis("wow", df["wow"].tolist())

    # 配置图表标题和工具箱
    line.set_global_opts(title_opts=opts.TitleOpts(title="对比dod和wow"),
                        toolbox_opts=opts.ToolboxOpts())

    # 保存图表为HTML文件
    file_path = "echarts_chart.html"
    # 渲染生成HTML文件
    line.render(file_path)
    return base_url + file_path


def draw_chart_image(data: str):
    """
    If the user's question mentions the need to draw chart image, you can call this function.
    Parameters:
        data: The data statement.(required)
    """
    if data == '' or data is None :
        return {"status": "false", "error": 'Data error, can not draw chart image'}
    # 将数据转换成DataFrame格式
    if(type(data) is str):
        df = pd.DataFrame(json.loads(data)) 
    else:
        df = pd.DataFrame(data)
    # 示例数据
    days = []
    for item in df["x"]:
        days.append(item.split(" ")[1].replace(":00",""))
    today_data = df["today"].tolist()
    dod_change = df["dod"].tolist()
    wow_change = df["wow"].tolist()

    # 创建子图
    fig, ax = plt.subplots(figsize=(10, 6))

    # 绘制今天数据
    # ax.bar(days, today_data, label='Today Data', color='blue')
    ax.plot(days, today_data, label='Today Data', marker='t', color='blue')
    # 绘制Day-Over-Day变化
    ax.plot(days, dod_change, label='Dod Change', marker='o', color='green')
    # 绘制Week-Over-Week变化
    ax.plot(days, wow_change, label='wow Change', marker='s', color='orange')

    # 添加标题和标签
    ax.set_title('数据概览')
    ax.set_xlabel('Day')
    ax.set_ylabel('Value/Change')
    ax.legend()

    # 显示图表
    plt.tight_layout()
    plt.savefig('./tmp/data_overview.png')
    plt.show()
    return './tmp/data_overview.png'