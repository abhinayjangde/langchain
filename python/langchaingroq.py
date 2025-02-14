import getpass
import os
from dotenv import load_dotenv
load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    print("Please set the GROQ_API_KEY environment variable.")
    exit()

from langchain.chat_models import init_chat_model

model = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")

result = model.invoke("hello")
print(result.content)