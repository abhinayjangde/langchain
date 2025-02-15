import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

chat_history = []
system_message = SystemMessage(content="You are an AI Chatbot and your name is codebhaiya."),

query = HumanMessage(content="Who are you ?")

chat_history.append(system_message)
chat_history.append(query)

res = model.invoke([chat_history])
print(res.content)
# while True:
#     query = input("You: ")
#     if query.lower() == "exit":
#         break
#     human_message = HumanMessage(content=query)

#     chat_history.append(human_message)
#     res = model.invoke(chat_history)

#     result = res.content

#     chat_history.append(AIMessage(content=result))

#     print("AI: ", result)


print("___________Chat History____________")
print(chat_history)