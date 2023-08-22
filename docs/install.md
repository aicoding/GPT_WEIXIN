# GPT_CodeInterpreter Project 🤖

GPT_CodeInterpreter is an AI-driven project designed to carry out various tasks related to code interpretation. It is built on a plugin architecture that can easily extend new features.

## Creating Plugins 👩‍💻👨‍💻

To create a plugin, follow these steps:

1. Create a new directory in the 'plugins' folder. The directory name will be the name of the plugin.

2. In the new directory, create a file named `functions.py`. In this file, define the functions you want the plugin to provide. Each function should be a top-level function and should be named in a way that reflects its functionality.

3. In the same directory, create a file named `config.json`. In this file, add the following JSON:

```json
{
    "enabled": true
}
```

This will enable the plugin by default. If you want to disable the plugin, you can change `true` to `false`.

## Running the Project 🏃‍♂️🏃‍♀️

To run this project, you need to follow these steps:

1. First, you need to create a `.env` file in the root directory of the project. You can do this by copying the `.env.example` file.

2. In the `.env` file, you need to provide your OpenAI API key. This should be a string, like `OPENAI_API_KEY=your_api_key_here`. Please replace `your_api_key_here` with your actual OpenAI API key.

3. Still in the `.env` file, you need to set the base URL for the OpenAI API. This should be a string, like `OPENAI_API_BASE=https://api.openai.com/v1`.

4. After saving the `.env` file, you need to install GPT_CodeInterpreter. You can do this with pip: `pip install -r requirements.txt`.

5. Once GPT_CodeInterpreter is installed, you can run the project with the following command: `chainlit run app.py`.

6. If `chainlit run app.py` error to communicate to openai,you can try `chainlit run app_cn.py`. 

Hope this display is more engaging and readable! If you have any other questions or need further assistance, feel free to let me know.

## Contributing

Contributions are welcome! Please read the contribution guide to learn how to contribute to this project.
