# GPT_CodeInterpreter 项目 🤖

GPT_CodeInterpreter 是一个基于人工智能的项目，设计用于执行与代码解释相关的各种任务。它建立在一个插件架构上，可以轻松扩展新的功能。

# 欢迎来到我的项目！👋
很高兴向你介绍我一直在努力的项目。这是一个托管在[此链接](https://chat.zhipenglu.repl.co)的聊天机器人。

## 如何使用 📚
要开始使用，访问 [https://chat.zhipenglu.repl.co](https://chat.zhipenglu.repl.co) 并输入你的查询或命令。这里有一些你可以使用的命令：
- **/set_api_key** - 设置你的 OPENAI_API_KEY 🔑
- **/set_model** - 设置你的 OPENAI_MODEL 🤖
- **/set_language** - 设置你的语言 🌍
- **/set_api_base** - 设置你的 OPENAI_API_BASE 🌐
- **/help** - 显示此帮助 📘

## 尽情享受吧！🎉
我希望你会发现这个聊天机器人有用且好玩。尽情享受吧！

## 📣 反馈与支持

🔧 **测试网站状态：** 测试网站托管在 Replit 上，并且是匆忙设置的。因此，它可能会偶尔出现停机或重启的情况。请放心，我正在积极改善其稳定性。

📬 **遇到问题了吗？** 如果测试网站关闭或者你遇到任何问题，请不要犹豫，[提出问题](https://github.com/boyueluzhipeng/GPT_CodeInterpreter/issues)。我会尽我所能尽快解决。

💡 **有建议或反馈吗？** 你的想法很重要！如果你有任何建议或反馈，我都愿意倾听。请通过[提出问题](https://github.com/boyueluzhipeng/GPT_CodeInterpreter/issues)分享你的想法。我会尽快回应并尽可能快地采纳有价值的反馈。

感谢你的理解和支持！🙏

## 关于 GPT_CodeInterpreter 的图片

![20230726150533](https://github.com/boyueluzhipeng/GPT_CodeInterpreter/assets/39090632/dabdf91f-0fc7-4794-bcdf-033f3e2dbafa)

![image](https://github.com/boyueluzhipeng/GPT_CodeInterpreter/assets/39090632/c5fac81b-7bbf-4bb8-83fe-4a0423eb3f86)

![image](https://github.com/boyueluzhipeng/GPT_CodeInterpreter/assets/39090632/ce360bb1-1347-4a96-a345-d15ddef618c2)

## 视频演示 🎥

https://github.com/boyueluzhipeng/GPT_CodeInterpreter/assets/39090632/d55503f7-f51c-4d0a-a284-e811eb5a98ac

## 项目特性

- **插件架构**：GPT_CodeInterpreter 使用了一个灵活且可扩展的插件架构。每个插件都是一个包含 `functions.py` 和 `config.json` 文件的文件夹，定义了插件的功能和配置。

### 🌟 即将推出的特性：

- **官方插件集成🔌**：通过处理官方源提供的标准 `openapi.yaml` ，我们可以自动获取相应的请求URL和方法名。这些将与本地函数结合，并发送给 GPT，就像调用本地特性一样。在用户调用时，我们将分类并请求相应的 API，确保实时和精确的反馈。

- **角色掩码🎭**：我们在本地插件中集成了许多基于角色的特性。例如，新添加的 `Vue` 插件可以用来轻松修改本地 Vue 项目。

- **加入我们的运动🤝**：我们正在积极邀请热情的个人与我们在这个项目上合作！让我们一起朝向 "metaGPT" 的未来，共同开发一系列令人着迷的角色插件。

### 🌈 未来计划：

- **多客户端交互🔗**：在运行多个客户端时，我们希望这些客户端能够交换消息，促进不同角色之间的数据传输。

  **初步概念💡**：

  - **服务器端⚙️**：由 GPT-4 "管理员" 预设角色操作，其主要职责将包括根据用户的 "角色掩码" 和预设目标分配任务，并随后评估任务完成率。

  - **客户端🖥️**：用户可以自主向服务器注册，并将能够接收派发的任务和任务完成率的反馈。它可以自主执行某些任务，也支持通过网页聊天接口进行交互以完成相关任务。

让我们期待这些新特性可以提供的无限可能性！🚀🎉

- **函数管理器**：函数管理器负责解析和调用每个插件的 `functions.py` 文件中定义的函数。

- **AI 驱动**：GPT_CodeInterpreter 利用 AI 的力量理解和生成人类语言，使其能够处理与代码解释相关的各种任务。

## 当前插件

1. **通用插件**：此插件提供了显示和上传图片的功能。

2. **Python 解释器插件**：此插件包含一个 Python 执行器，用于运行 Python 代码，这对于数据分析和表处理等任务非常有用。

3. **Vue 插件**：目前正在开发中，此插件设计用于与 Vue 项目一起工作，通过聊天界面自动化整个 Vue 项目的修改。

## 文档

要开始使用 GPT_CodeInterpreter，请参考以下文档：

- 📚 [如何安装和使用 GPT_CodeInterpreter](docs/install_CN.md)：学习如何在你的项目中安装和使用 GPT_CodeInterpreter。

- 🚀 [在 Replit 上发布 GPT_CodeInterpreter](docs/replit_CN.md)：关于在 Replit 平台上发布 GPT_CodeInterpreter 的逐步指南。

- 📝 [理解环境变量](docs/env_CN.md) - 🔑 使用必要的环境变量配置 GPT_CodeInterpreter。

## 贡献

欢迎贡献！请阅读贡献指南，了解如何向此项目贡献。

## 联系

对于任何查询或合作机会，你可以通过电子邮件 `402087139@qq.com` 联系我。📧

## 许可

该项目在 MIT 许可的条款下授权。📜
