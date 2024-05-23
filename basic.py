import google.generativeai as genai
import os

genai.configure(api_key=os.getenv('GEMINI_API_KEY') or "")


# will list available models
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-pro')

response =model.generate_content("What is the future of AI in one sentence?")

print(response.text)
print(response.prompt_feedback)
print(response.candidates)

response = model.generate_content("What is the future of AI in one sentence?", stream=True)

for chunk in response:
  print(chunk.text)
  print("_"*80)