import chainlit as cl
import requests
import json
from functions.date import date_convertion
from functions.file import generate_charts_file,draw_chart_image,write_file
from functions.xlog import XLOG_API_DOMAIN,XLOG_API_HEADERS,query_metric_config_list_from_xlog,query_metric_data_detail_from_xlog

async def query_metric_config_list_from_xlog(metricName: str):
    """
    输入一个指标名称,从xlog系统里查询相关指标配置的列表,该方法会返回指标列表的集合数据,输入具体时间日期、TODAY、DOD和WOW不要调用该方法
    Parameters:
        metricName: The metricName statement.(required)
    """
    try:
        if metricName == '':
            return {"status": "false", "error": "请输入指标名称"}
        url = XLOG_API_DOMAIN + "/admin/middle/metric/config/list?metricNameCn=" + metricName
        print(f"url==={url}")
        response = requests.get(url, headers = XLOG_API_HEADERS)

        if response.status_code != 200:
            raise Exception("Non-200 response: " + str(response.text))
        response_json = response.json()
        if response_json['code'] != 200:
            raise Exception("Non-200 response: " + str(response_json['msg']))

        response_data = response_json['content']
        elments = []
        actions = []
        if(response_data):
             response_data = [item for item in response_data if item['metricGroup'] != "sz_llpt" and item['metricGroup'] !="tapi_group"]

        for item in response_data:
            # metric = "指标名称:"+item['metricNameCn']+";指标ID:"+str(item['id'])+";指标条件:"+item['metricCondition']
            metric = "指标名称:"+item['metricNameCn']+";指标ID:"+str(item['id'])
            elments.append(cl.Text(content=metric,display="inline"))
            actions.append(cl.Text(content=metric,display="inline"))    
        # res = await cl.AskUserMessage(content="请选择一个指标?", timeout=10).send()
        # if res:
        #     await cl.Message(
        #         content=f"选择的指标是: {res['content']}",
        #     ).send() 
        await cl.Message(content="查找到以下相关指标：",elements=elments,prompt="请换行以列表方式展示").send()
        # await cl.Message(content="查找到指标列表：",elements=elments,actions=actions,prompt="请换行以列表方式展示").send()
        return response_data
    except Exception as e:
        return {"status": "false", "error": str(e)}
    

async def query_metric_data_detail_from_xlog(metricId: int, start: str, end: str):
    """
    输入指标一个指标id,从xlog系统里查询指标id对应的数据明细,该方法会返回该指标id对应的数据明细
    Parameters:
        metricId: The metricId statement.(required)
        start: The start date statement.(required)
        end: The end date statement.(required)
    """
    try:
        startDate = date_convertion(start)
        endDate = date_convertion(end)
        if startDate == '' or endDate == '':
            raise Exception("Date format error: start=" + start + "&end=" + end)
        if (startDate.startswith('2023-')== False or endDate.startswith('2023-') == False):
            return {"status": "false", "Description": "需要给个时间段", "error":"Date format error: start=" + start + "&end=" + end}
        # if(interval=='' or interval.endswith("m")== False or interval.endswith("h")== False or interval.endswith("d")== False):
        #    interval = "5m"
        data = {
            "metricId": metricId,
            "interval": "5m",
            "searchType": "histogram",
            "days": 2,
            "start": startDate,
            "end": endDate
        }
        print(data)
        # return {"status": "false", "data": data}
        response = requests.post(XLOG_API_DOMAIN + "/admin/metric/search",headers = XLOG_API_HEADERS,data = json.dumps(data))
        response_json = response.json()
        if response_json['code'] != 200:
            raise Exception("Non-200 response: " + str(response_json['msg']))

        response_json = response.json()
 
        response_data = {
            'x':response_json['content']['x'],
            'today':response_json['content']['today'],
            'dod':response_json['content']['dod'],
            'wow':response_json['content']['wow'],
        }
        elments = []
        todayTotal = sum(response_json['content']['today'])
        dodTotal = sum(response_json['content']['dod'])
        wowTotal = sum(response_json['content']['wow'])
        #给个总数的描述
        totalStr = "today总数:" + str(todayTotal) + ",dod总数:" + str(dodTotal) + ",wow总数:" + str(wowTotal)
        #给画一个图表
        image_url = draw_chart_image(response_data);
        tmp_image = cl.Image(name=f"image{metricId}",path=image_url.strip(),display="inline")
        tmp_image.size = "large"
        elments.append(tmp_image)
        #给生成一个echarts图表
        file_url = generate_charts_file(response_data)
        #结果写在文件里
        #write_file(f"metric_{metricId}.json",response_data)
        #显示在UI视图
        await cl.Message(content="数据汇总:"+totalStr+"\n echarts地址:"+file_url,elements=elments).send()
        return {"数据汇总":totalStr,"file_url":file_url,"image_url":image_url}
    except Exception as e:
        return {"status": "false", "error": str(e)}

    

#请求指标以柱状图汇总的方式返回today,dod,wow数据    
# async def search_metric_data_detail_from_xlog(metricName:str, metricId: int, start: str, end: str, interval:str):
#     """
#     If the user's question mentions the need to get metric data detail from the xlog, you can call this function.
#     Parameters:
#         metricName: The metricName statement.(required)
#         metricId: The metricId statement.(required)
#         start: The start date statement.(required)
#         end: The end date statement.(required)
#         interval: The interval statement.(required)
#     """
#     try:
#         responseData = ''
#         if(metricName):
#             responseData = await query_metric_config_list_from_xlog(metricName);
#         else:
#             responseData = await query_metric_data_detail_from_xlog(metricId,start,end,interval)
#         responseData = str(json.dumps(responseData)).encode('utf-8').decode('utf-8')
#         await cl.Message(content=responseData).send()
#         return responseData
#     except Exception as e:
#         return {"status": "false", "error": str(e)}

