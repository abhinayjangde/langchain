import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

messages = [
    SystemMessage(content="You are an AI Chatbot and your name is codebhaiya."),
    HumanMessage(content="Who are you ?")
]

res = model.invoke(messages)
print(res.content)