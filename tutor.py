import tkinter as tk
from tkinter import scrolledtext
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableMap

# Model setup
model = OllamaLLM(
    model="gemma2:2b",
    temperature=0.6,
    top_k=30,
    repeat_penalty=2
)

# Prompt template
template = """
You are a tutor, named TUTORBOT. You keep things simple, and casual, you talk to your students informally. Re-explain this work in simple casual terms, in as little words as possible thats still understandable gramatically.
Here’s the work:
'{question}'
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# GUI setup
def simplify_text():
    input_text = input_box.get("1.0", tk.END).strip()
    if input_text:
        output_box.delete("1.0", tk.END)
        result = chain.invoke({"question": input_text})
        output_box.insert(tk.END, result)

# Window
window = tk.Tk()
window.title("Text Simplifier with Vibes")

# Input label and text area
tk.Label(window, text="Paste work here:").pack()
input_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=10)
input_box.pack(padx=10, pady=5)

# Simplify button
tk.Button(window, text="Simplify It", command=simplify_text).pack(pady=5)

# Output label and text area
tk.Label(window, text="Simplified Output:").pack()
output_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=10)
output_box.pack(padx=10, pady=5)

# Run the app
window.mainloop()
