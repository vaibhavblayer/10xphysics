import base64
import requests
import os

api_key = os.environ["OPENAI_API_KEY"]


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


# Path to your image
image_1_path = "main-6.png"
image_2_path = "main-2.png"

# Getting the base64 string
base64_image_1 = encode_image(image_1_path)
base64_image_2 = encode_image(image_2_path)

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "can you extract this question from image in latex format? serial wise question number and question should be in enumerate env. extract all the questions from 66 to 75. Don't include exam appearance. Only give me the enumerate part not the whole latex file."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{base64_image_1}"
                    }
                },
                # {
                #     "type": "image_url",
                #     "image_url": {
                #         "url": f"data:image/png;base64,{base64_image_2}"
                #     }
                # }
            ]
        }
    ],
    "max_tokens": 2000
}

response = requests.post(
    "https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json()["choices"][0]["message"]["content"])
