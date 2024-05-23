import PIL.Image
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv('GEMINI_API_KEY') or "")
img = PIL.Image.open('Taj_Mahal.png')
model = genai.GenerativeModel('gemini-pro-vision')
response = model.generate_content(img)
response = model.generate_content(["Write a short, engaging blog artile based on this picture.", img], stream=False)
response.resolve()
print(response.text)