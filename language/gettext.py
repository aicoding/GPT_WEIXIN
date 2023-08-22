# gettext.py
import json
import os

def get_text(language, key):
    # 创建一个字典来映射语言别名到文件名
    language_map = {
        "en": "en",
        "english": "en",
        "cn": "zh_CN",
        "chinese": "zh_CN",
        "zh": "zh_CN",
    }

    # 获取对应的文件名
    file_name = language_map.get(language.lower())

    if file_name is None:
        raise ValueError(f"Unsupported language: {language}")

    # 创建文件路径
    file_path = os.path.join(os.path.dirname(__file__), f"{file_name}.json")

    # 打开并读取 JSON 文件
    with open(file_path, 'r', encoding='utf-8') as file:
        translation = json.load(file)

    # 返回指定键的翻译文本
    return translation.get(key)
