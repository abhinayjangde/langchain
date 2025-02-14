import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "who is the president of the united states?",
        }
    ],
    model="deepseek-r1-distill-qwen-32b",
)

print(chat_completion.choices[0].message.content)



