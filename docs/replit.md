## Use Replit to deploy 🚀

### Step 1: Deploy to Repl.it

Click the button below to deploy this project to Replit:

[![Run on Replit](https://replit.com/badge/github/boyueluzhipeng/GPT_CodeInterpreter)](https://replit.com/new/github/boyueluzhipeng/GPT_CodeInterpreter)

Once you've clicked the button, the project repository will be cloned into a new Replit workspace.

### Step 2: Install Dependencies 📦

After the project has been cloned, you need to install the necessary dependencies. To do this, open the Shell terminal in Replit, and run the following command:

```bash
pip install -r requirements.txt
```

This will install all the Python packages listed in the `requirements.txt` file.

### Step 3: Configure Environment Variables ⚙️

Next, you need to set up the environment variables. In the Shell terminal, run the following command:

```bash
cp .env.example .env
```

This command copies the contents of the `.env.example` file into a new file named `.env`.

### Step 4: Add Secrets 🔐

Then, go to the 'Secrets' section in Replit (usually on the left sidebar), and select 'Edit as JSON'. Copy and paste the following JSON content:

```json
{
  "OPENAI_API_KEY": "your_api_key",
  "OPENAI_API_BASE": "https://api.openai.com/v1"
}
```

Replace `"your_api_key"` with your actual OpenAI API key.

### Step 5: Run the Project ▶️

Now, you're ready to run the project. Click the 'Run' button at the top of the Replit interface.

### Step 6: Access the Web Interface 🌐

Once the project is running, find your public URL in the 'Webview' section. You can use this URL to access the GPT Code Interpreter in your web browser.

And that's it! You've successfully deployed the GPT Code Interpreter on Replit. If you encounter any issues, please refer to the Replit documentation or raise an issue on the project's GitHub page.