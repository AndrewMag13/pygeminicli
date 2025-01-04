import google.generativeai as genai
from rich.console import Console
from rich.markdown import Markdown

genai.configure(api_key="YOUR API HERE")
console = Console()
console.print("[bold cyan]##### Welcome to pyGeminiCli! #####[/bold cyan]\nThis version works with Gemini-1.5-flash!\nTo exit press Ctrl+C\nEnjoy!\n")
model = genai.GenerativeModel("gemini-1.5-flash")
while True:
  response = model.generate_content(input("Text your question here\n"))
  console.print(Markdown(response.text))