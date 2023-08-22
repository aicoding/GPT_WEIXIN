# 环境变量
此项目使用以下环境变量在 `.env` 文件中：

## `OPENAI_API_KEY`
- 访问 OpenAI API 所需的 OpenAI API 密钥。

## `OPENAI_API_BASE`
- OpenAI API 的基本 URL。无需操作，设置为 `https://api.openai.com/v1`。

## `OPENAI_MODEL`
- 用于 GPT-3.5 Turbo API 语言生成的模型变体。

## `MAX_TOKENS`
- 在单个 API 调用中允许的最大 token 数量。默认：5000。

## `LANGUAGE`
- 与 GPT-3.5 Turbo 模型进行交流的语言。默认：英语。

请确保将 `LANGUAGE` 变量设置为您希望在与 GPT-3.5 Turbo 模型交互时使用的语言。
