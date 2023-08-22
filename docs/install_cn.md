# GPT_CodeInterpreter Project 🤖

GPT_CodeInterpreter 是一个AI驱动的项目，旨在执行各种代码解释相关的任务。它建立在插件架构之上，可以轻松扩展新功能。

## 创建插件 👩‍💻👨‍💻

要创建一个插件，请按照以下步骤进行：

1. 在 'plugins' 文件夹中创建一个新目录。目录名称将成为插件的名称。

2. 在新目录中创建一个名为 `functions.py` 的文件。在此文件中，定义您想要插件提供的功能函数。每个函数应为顶级函数，并以反映其功能的方式命名。

3. 在同一目录中，创建一个名为 `config.json` 的文件。在此文件中添加以下 JSON：

```json
{
    "enabled": true
}
```

这将默认启用插件。如果您想禁用插件，可以将 `true` 更改为 `false`。

## 运行项目 🏃‍♂️🏃‍♀️

要运行此项目，您需要按照以下步骤操作：

1. 首先，在项目的根目录中创建一个 `.env` 文件。您可以通过复制 `.env.example` 文件来实现。

2. 在 `.env` 文件中，您需要提供您的 OpenAI API 密钥。这应该是一个字符串，类似于 `OPENAI_API_KEY=your_api_key_here`。请将 `your_api_key_here` 替换为您的实际 OpenAI API 密钥。

3. 在 `.env` 文件中，您还需要设置 OpenAI API 的基本 URL。这应该是一个字符串，类似于 `OPENAI_API_BASE=https://api.openai.com/v1`。

4. 保存 `.env` 文件后，您需要安装 GPT_CodeInterpreter。您可以使用 pip 进行安装：`pip install -r requirements.txt`。

5. 安装完成后，您可以通过以下命令运行项目：`chainlit run app.py`。

希望这样的显示更加生动和易读！如果您有其他问题或需要进一步的帮助，请随时告诉我。
