import getpass
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

load_dotenv()

# Old Code Without Memory
'''if not os.getenv("GROQ_API_KEY"):
    print("Please set the GROQ_API_KEY environment variable.")
    exit()


model = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")


# response = model.invoke([HumanMessage(content="Hi, I'm Abhinay")])
# response = model.invoke([HumanMessage(content="What's my name?")])
response = model.invoke([
    HumanMessage(content="Hi, I'm Abhinay"),
    AIMessage(content="Hello, Abhinay! How can I help you today?"),
    HumanMessage(content="What's my name?")
])
print(response.content)

'''


# New Code With Memory

if not os.getenv("GROQ_API_KEY"):
    print("Please set the GROQ_API_KEY environment variable.")
    exit()

model = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")

# define a new graph

workflow = StateGraph(state_schema=MessagesState)

# defines the function that calls the model

def call_model(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"response": response}

# define the (single) node in the graph

workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

# add memoery

memory = MemorySaver()

app = workflow.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "abc123"}}

query = "Hi! I'm Abhinay."

input_messages = [HumanMessage(query)]
output = app.invoke({"messages": input_messages}, config)
# output["messages"][-1].pretty_print()  # output contains all messages in state
print(output["messages"][-1].pretty_print())


query = "What's my name?"

input_messages = [HumanMessage(query)]
output = app.invoke({"messages": input_messages}, config)
output["messages"][-1].pretty_print()