
import json
import re
from functions.MakeRequest import get_api_info, get_md5
import globale_values as gv
import chainlit as cl

async def bind_user_plugin():
    """
    if user want to bind his own plugin, you can call this function.
    Parameters: None
    """
    res = await cl.AskUserMessage(content="请给我一个fastapi服务的地址，例如：http://127.0.0.1:8000").send()
    # 判断用户输入的是否是一个合法的url
    if res is None:
        return {'description': '您没有输入任何内容'}
    if not re.match(r'^https?:/{2}\w.+$', res['content']):
        return {'description': '您输入的不是一个合法的url'}
    api_info = get_api_info(res['content'])
    if len(api_info) == 0:
        return {'description': '获取api信息失败'}
    url_md5 = get_md5(res['content'])
    final_dit = {
        "url": res['content'],
        "api_info": api_info,
        'url_md5': url_md5,
    }
    user_plugin_api_info = cl.user_session.get('user_plugin_api_info')
    if user_plugin_api_info is None:
        user_plugin_api_info = []
    user_plugin_api_info.append(final_dit)
    
    cl.user_session.set('user_plugin_api_info', user_plugin_api_info)
    return {'description': '插件绑定成功'}


async def bind_chatgpt_plugin():
    """
    if user want to bind chatgpt plugin, you can call this function.
    """
    res = await cl.AskUserMessage(content="请前往https://plugins.zhipenglu.repl.co 选择适合的插件，点击图片复制plugin id,输入到输入框内").send()
    # 读取plugins/common/my_apis.json文件
    if gv.chatgpt_plugin_info is None:
        with open('plugins/serverplugin/my_apis.json', 'r') as f:
            gv.chatgpt_plugin_info = json.load(f)
    plugin_info = gv.chatgpt_plugin_info
    print('共有{}个插件'.format(len(plugin_info)))
    # 判断用户输入的plugin id是否存在
    for item in plugin_info:
        if res is None:
            return {'description': '您没有输入任何内容'}
        if item['id'] == res['content']:
            
            for api in item['apis']:
                if 'original_name' in api:
                    # 删除original_name
                    del api['original_name']
                if 'request_endpoint' in api:
                    # 删除request_endpoint
                    del api['request_endpoint']
                if 'method' in api:
                    # 删除method
                    del api['method']
            # 保存到session中
            final_dit = {
                "url": item['url'],
                "api_info": item['apis'],
                'url_md5': item['url_md5'],
            }
            user_plugin_api_info = cl.user_session.get('user_plugin_api_info')
            if user_plugin_api_info is None:
                user_plugin_api_info = []
            user_plugin_api_info.append(final_dit)
            print("==================================")
            print(user_plugin_api_info)
            print("==================================")
            cl.user_session.set('user_plugin_api_info', user_plugin_api_info)
            return {'description': '插件绑定成功'}
    return {'description': '您输入的plugin id不存在'}


async def clear_all_plugins():
    """
    if user want to clear all plugins, you can call this function.
    Parameters: None
    """
    cl.user_session.set('user_plugin_api_info', None)
    return {'description': '清除成功'}