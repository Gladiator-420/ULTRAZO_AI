from groq import Groq
import os
print("WELCOME to Ultrazo AI")
client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

messages = [
    {
        "role": "system",
        "content": "You are an intelligent assistant named Ultrazo."
    }
]

while True:
    user_message = input("User: ")
    if user_message:
        messages.append(
            {
                "role": "user",
                "content": user_message,
            }
        )
        
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=messages
        )
        
        reply = completion.choices[0].message.content
        
        messages.append(
            {
                "role": "assistant",
                "content": reply,
            }
        )
        
        # Printing the assistant's reply
        print(f"Ultrazo: {reply}")
