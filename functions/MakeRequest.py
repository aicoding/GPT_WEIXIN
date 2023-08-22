import requests
import json
from collections import OrderedDict
import hashlib
import globale_values as gv

def request_plugin_api(method, base_url, arguments=None):
    if arguments is None:
        arguments = {}

    # 存储已经替换过的key
    replaced_keys = []

    # 检查URL中是否有占位符，并进行替换
    for key, value in arguments.items():
        placeholder = "{" + key + "}"
        if placeholder in base_url:
            base_url = base_url.replace(placeholder, str(value))
            replaced_keys.append(key)

    # 从参数中移除已替换过的key
    for key in replaced_keys:
        del arguments[key]

    print("===========request_plugin_api=============")
    print(base_url, arguments, method)
    print("==========================================")
    if method == 'get':
        response = requests.get(base_url, params=arguments)
    elif method == 'post':
        response = requests.post(base_url, json=arguments)
    elif method == 'put':
        response = requests.put(base_url, json=arguments)
    elif method == 'delete':
        response = requests.delete(base_url, params=arguments)
    elif method == 'options':
        response = requests.options(base_url)
    elif method == 'head':
        response = requests.head(base_url)
    elif method == 'patch':
        response = requests.patch(base_url, json=arguments)
    else:
        response = None

    if response is None:
        return {
            'description': '请求失败'
        }
    
    print("==================================")  
    print(response.text) 
    print("==================================") 

    if response.status_code == 200:
        return response.text
    else:
        return {"status_code": response.status_code, "text": response.text}

def make_request(api_url, method, function_name, arguments):
    request_url = api_url + '/' + function_name
    print(request_url, method, arguments)
    if type(arguments) == str:
        arguments = json.loads(arguments)
    return request_plugin_api(method, request_url, arguments)
   
    
def make_request_chatgpt_plugin(plugin_id, name, arguments):
    if gv.chatgpt_plugin_info is None:
        with open('plugins/serverplugin/my_apis.json', 'r') as f:
            gv.chatgpt_plugin_info = json.load(f)
    plugin_info = gv.chatgpt_plugin_info
    print('共有{}个插件'.format(len(plugin_info)))
    print(plugin_id, name, arguments)
    # 判断用户输入的plugin id是否存在
    for item in plugin_info:
        if item['id'] == plugin_id:
            for api in item['apis']:
                if api['name'] == name:
                    print(api['request_endpoint'], api['method'], arguments)
                    if type(arguments) == str:
                        arguments = json.loads(arguments)
                    return request_plugin_api( api['method'], api['request_endpoint'], arguments)

def get_md5(url):
    md5 = hashlib.md5()
    md5.update(url.encode('utf-8'))
    return md5.hexdigest()[:8]

def get_api_info(api_url):
    response = requests.get(api_url + "/openapi.json")
    data = response.json()

    api_info = []
    api_url_md5 = get_md5(api_url)
    for path, path_info in data["paths"].items():
        for method, method_info in path_info.items():
            if method in ["get", "post", "put", "delete", "options", "head", "patch", "trace"]:
                parameters = method_info.get("parameters", [])
                if method in ["post", "put", "patch"]:
                    if "requestBody" in method_info:
                        content = method_info["requestBody"].get("content", {})
                        if "application/json" in content:
                            schema = content["application/json"].get("schema", {})
                            if "$ref" in schema:
                                ref_path = schema["$ref"]
                                components_path = ref_path.split("/")[1:]
                                schema = data
                                for component in components_path:
                                    schema = schema.get(component, {})
                            if "title" in schema:
                                del schema["title"]
                            ordered_schema = OrderedDict()
                            for key in ["type", "properties", "required"]:
                                if key in schema:
                                    ordered_schema[key] = schema[key]
                            parameters.append(ordered_schema)

                func_info = {
                    "name": f"{path[1:]}_{method}_{api_url_md5}",
                    "description": method_info.get("description", ""),
                    "parameters": parameters
                }
                api_info.append(func_info)
    
    # remove "title" and "default" from properties and make parameters a dictionary
    final_api_info = []
    for api in api_info:
        if '.' in api['name']:
            continue
        parameters_dict = {
            "type": "object",
            "properties": {},
            "required": []
        }
        for param in api['parameters']:
            propertys = {}
            if 'properties' in param:
                for prop_name, prop_info in param['properties'].items():
                    if 'title' in prop_info:
                        del prop_info['title']
                    if 'default' in prop_info:
                        del prop_info['default']
                    propertys[prop_name] = prop_info
                parameters_dict['type'] = param['type']
                parameters_dict['properties'] = propertys
                parameters_dict['required'] = param['required']
            
        api['parameters'] = parameters_dict
        final_api_info.append(api)

    try:
        response = json.loads(json.dumps(final_api_info, indent=2))
    except:
        response = []
    print('=' * 100)
    print(response)
    print('=' * 100)
    return response


# r = make_request("https://gift.pluginbuilders.repl.co","get", "legal",{})
# print(r)
