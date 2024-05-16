import base64
import requests
import os

api_key = os.environ["OPENAI_API_KEY"]


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


# Path to your image
image_1_path = "img.jpg"
# image_2_path = "main-2.png"

# Getting the base64 string
base64_image_1 = encode_image(image_1_path)
# base64_image_2 = encode_image(image_2_path)

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
                    "text": "can you draw this diagram in tikz? Only give me the tikz part not the whole latex document."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image_1}"
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
