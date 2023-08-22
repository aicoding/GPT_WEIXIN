## 使用 Replit 部署 🚀

### 步骤 1: 部署到 Replit

点击下面的按钮将此项目部署到 Replit：

[![在 Replit 上运行](https://replit.com/badge/github/boyueluzhipeng/GPT_CodeInterpreter)](https://replit.com/new/github/boyueluzhipeng/GPT_CodeInterpreter)

点击按钮后，项目仓库将被克隆到一个新的 Replit 工作空间。

### 步骤 2: 安装依赖 📦

在项目被克隆后，您需要安装必要的依赖。在 Replit 中打开 Shell 终端，并运行以下命令：

```bash
pip install -r requirements.txt
```

这将安装在 `requirements.txt` 文件中列出的所有 Python 包。

### 步骤 3: 配置环境变量 ⚙️

接下来，您需要设置环境变量。在 Shell 终端中运行以下命令：

```bash
cp .env.example .env
```

此命令将 `.env.example` 文件的内容复制到一个名为 `.env` 的新文件中。

### 步骤 4: 添加密钥 🔐

然后，前往 Replit 中的 'Secrets' 部分（通常在左侧边栏），并选择 'Edit as JSON'。复制并粘贴以下 JSON 内容：

```json
{
  "OPENAI_API_KEY": "your_api_key",
  "OPENAI_API_BASE": "https://api.openai.com/v1"
}
```

将 `"your_api_key"` 替换为您的实际 OpenAI API 密钥。

### 步骤 5: 运行项目 ▶️

现在，您已经准备好运行项目了。在 Replit 界面的顶部点击 'Run' 按钮。

### 步骤 6: 访问 Web 界面 🌐

项目运行后，在 'Webview' 部分找到您的公共 URL。您可以使用此 URL 在 web 浏览器中访问 GPT Code Interpreter。

就是这样！您已经成功在 Replit 上部署了 GPT Code Interpreter。如果遇到任何问题，请参阅 Replit 文档或在项目的 GitHub 页面提出问题。

希望这个翻译对您有帮助！如果您还有其他问题或需要进一步帮助，请随时告诉我。