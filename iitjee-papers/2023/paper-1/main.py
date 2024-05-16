import PIL.Image
import os
import google.generativeai as genai

# Get the API key from an environment variable
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)


for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)


model = genai.GenerativeModel('gemini-pro-vision')

img = PIL.Image.open('Screen Shot 1.png')
img2 = PIL.Image.open('Screen Shot 2.png')
response = model.generate_content(
    ["Analyse this image and extract question in latex format. Can you make those diagrams using tikz.", img, img2], stream=True)
response.resolve()

print(response.text)
