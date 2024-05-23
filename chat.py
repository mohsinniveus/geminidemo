import google.generativeai as genai
import os


#In one sentence, explain how a computer works to a young child.
#Okay, how about a more detailed explanation to a high schooler?

genai.configure(api_key=os.getenv('GEMINI_API_KEY') or "")

model = genai.GenerativeModel('gemini-pro')

chat = model.start_chat(history=[])

while True:
    user_input = input("You: ")
    response = chat.send_message(user_input, stream=True)
    for chunk in response:
        print(chunk.text)