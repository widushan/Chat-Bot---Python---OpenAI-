import os
from dotenv import load_dotenv
from litellm import completion
import tkinter as tk
from tkinter import scrolledtext
import textwrap

# Load environment variables from .env file
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Function to format text nicely for humans
def format_text(text):
    # Split text into sentences
    sentences = text.split('. ')
    formatted = ""
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            # Add bullet point if sentence seems like a list point
            if any(word in sentence.lower() for word in ["such as", "including", "like"]):
                formatted += "• " + sentence + ".\n"
            else:
                formatted += sentence + ".\n"
    # Wrap lines at 80 characters for easier reading
    return "\n".join(textwrap.fill(line, width=80) for line in formatted.splitlines())

# Function to get response from LiteLLM
def get_response(event=None):
    user_input = user_entry.get()
    if not user_input.strip():
        return

    output_text.config(state='normal')
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "Thinking...")
    output_text.config(state='disabled')
    user_entry.delete(0, tk.END)

    root.update()  # Update GUI to show "Thinking..." before processing
    messages = [{"content": user_input, "role": "user"}]
    try:
        response = completion(
            model="openai/gpt-3.5-turbo",
            messages=messages
        )
        answer = response['choices'][0]['message']['content']
        formatted_answer = format_text(answer)
        output_text.config(state='normal')
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, formatted_answer)
        output_text.config(state='disabled')
    except Exception as e:
        output_text.config(state='normal')
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Error: {e}")
        output_text.config(state='disabled')

# Create GUI window
root = tk.Tk()
root.title("LiteLLM Chat")
root.geometry("500x400")

# Input label and entry
tk.Label(root, text="Type your question:").pack(pady=5)
user_entry = tk.Entry(root, width=60)
user_entry.pack(pady=5)
user_entry.bind("<Return>", get_response)  # Enter key submits

# Submit button
tk.Button(root, text="Get Answer", command=get_response).pack(pady=5)

# Output area
tk.Label(root, text="Answer:").pack(pady=5)
output_text = scrolledtext.ScrolledText(root, height=15, width=60, state='disabled', wrap=tk.WORD)
output_text.pack(pady=5)

# Run the GUI loop
root.mainloop()
