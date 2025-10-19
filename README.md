# Chat Bot 🤖 (Python + OpenAI)

A small, local Python chat-bot example that uses OpenAI-style APIs. This repository contains a lightweight demo showing how to wire a simple chat interface to an LLM backend using Python.

Key points
- Minimal, easy-to-follow code in `app.py`.
- Single-file demo suitable for learning and quick experimentation.
- Requirements are listed in `requirements.txt`.

---

## Features

- Send user messages to an LLM backend
- Simple configuration via environment variables
- Ready to be extended into a web or CLI chat app

## Prerequisites

- Python 3.10+ (recommended)
- pip
- An API key for your chosen LLM provider (set as an environment variable; see Configuration)

Install dependencies:

```powershell
pip install -r requirements.txt
```

> Note: `requirements.txt` currently lists `litellm`. If you use a different library (openai, langchain, etc.), update dependencies accordingly.

## Configuration

Set your LLM API key as an environment variable before running the app. Example (PowerShell):

```powershell
$env:OPENAI_API_KEY = "your_api_key_here"
```

Replace `OPENAI_API_KEY` with whatever variable your code expects (check `app.py`).

## Usage

Run the chat app from the project root:

```powershell
python app.py
```

Follow the prompts in the terminal (or open the UI if `app.py` serves one).

## Screenshots

<img width="498" height="429" alt="Image" src="https://github.com/user-attachments/assets/f8837380-d9c5-4bd1-a1b1-8d2d1a725642" />

<img width="496" height="422" alt="Image" src="https://github.com/user-attachments/assets/3554267f-af10-4356-a7b6-b009040061c4" />

<img width="499" height="425" alt="Image" src="https://github.com/user-attachments/assets/a6fb0074-409b-47d2-8102-cbb17902e438" />

## Add this project to GitHub (PowerShell)

Create a new repository on GitHub (via web UI or gh CLI), then run these commands from the project root in PowerShell to push the code:

```powershell
# initialize git repo (if not already initialized)
git init
# add files and commit
git add .
git commit -m "Initial commit"
# add remote (replace URL with your repository URL)
git remote add origin https://github.com/widushan/Chat-Bot---Python---OpenAI-.git
# push to main (create branch if needed)
git branch -M main
git push -u origin main
```

If you use SSH, replace the remote URL with the SSH form:

```powershell
git remote add origin git@github.com:<your-username>/<your-repo>.git
git push -u origin main
```

## Contributing

- Open an issue for bugs or feature requests.
- Send a pull request with a clear description of changes.

## Troubleshooting

- If dependencies fail to install, upgrade pip: `python -m pip install --upgrade pip`.
- If the app can't find an API key, double-check the environment variable name and restart your shell.

## License & Contact

Include a license file if you want to make this project open source (for example, `LICENSE` with MIT). For questions, open an issue or contact the repository owner.
widushanp@gmail.com

---

Happy hacking! 🎯
