# 🚀 CodeBot

CodeBot is a powerful tool that lets you run code from the command line. Simply install our PyPI package and run it from the command line.

## Installation

We have released a new PyPI package called `codebot`, version `0.0.5`. You can install it using pip:

```bash
pip install codebot==0.0.5
```

This package includes several dependencies such as `chainlit`, `loguru`, `tiktoken`, `prompt_toolkit`, `jupyter`, `mysql-connector-python`, `pillow`, and `pyngrok`.

## Usage

Once you have installed the `codebot` package, you can run code from the command line. This is done through the `console_scripts` entry point in our `setup.py` file.

```bash
codebot
```

## Configuration

The `codebot` tool uses a configuration file stored at `~/.codebot/config.json`. The configuration includes options for OpenAI API base, API key, model, max tokens, and language. You can modify these options to suit your needs.

If the configuration file does not exist or the API key is not set, the tool will prompt you for the necessary information.

## Ngrok Integration

The `codebot` tool now supports ngrok integration. If you provide an ngrok auth token, the tool will create an ngrok tunnel to port 8000. This is very useful for exposing your local development server to the internet.

## Reset Configuration

The `codebot` tool provides a `--config` option to reset the configuration. If this option is given, the tool will delete the existing configuration file and create a new one.

## Fix Mode

The `codebot` tool provides a `--fix` option to run the application in fix mode. If this option is given, the tool will run `app_cn.py`, otherwise, it will run `app.py`.

## Parameter Passing

The `codebot` tool provides several command-line arguments to control its behavior:

- `--fix`: This argument makes `codebot` run the application in fix mode. If this argument is given, the tool will run `app_cn.py`, otherwise, it will run `app.py`.
- `--ngrok`: This argument allows you to provide an ngrok auth token. If this argument is given, the tool will create an ngrok tunnel to port 8000.
- `--config`: This argument is used to reset the configuration. If this argument is given, the tool will delete the existing configuration file and create a new one.

You can provide these arguments when running the `codebot` command. For example, if you want to run the application in fix mode and set the ngrok auth token, you can run:

```bash
codebot --fix --ngrok YOUR_NGROK_AUTH_TOKEN
```

Replace `YOUR_NGROK_AUTH_TOKEN` with your ngrok auth token.

We hope you find these updates helpful. As always, if you have any feedback or suggestions, let us know!
