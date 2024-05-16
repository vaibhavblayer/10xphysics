import requests
import os

api_key = os.getenv("OPENAI_API_KEY")


def process_text(input_file: str, prompt: str, api_key: str, max_tokens: int) -> str:
    """
    Processes text using OpenAI's GPT-4, extracts LaTeX code from the response,
    copies the first match to the clipboard, and prints the message in deep pink color.

    Args:
        input_file (str): Path to the input file to be processed.
        prompt (str): Prompt for the GPT-4 model.
        api_key (str): OpenAI API key.
        max_tokens (int): Maximum number of tokens to generate.

    Returns:
        str: First match of the LaTeX code in the response.
    """
    with open(input_file, 'r') as file:
        input_text = file.read()

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
                        "text": prompt
                    },
                    {
                        "type": "text",
                        "text": input_text
                    }
                ]
            }
        ],
        "max_tokens": max_tokens
    }

    message = ""

    response = requests.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        response_json = response.json()

        if 'choices' in response_json and 'message' in response_json["choices"][0]:
            message = response_json["choices"][0]["message"]["content"]

    return message


prompt = r"""
Following problem in in latex format, Please analyze the following questions and if possible solve the problem and provide the solution in LaTeX format as well. Just below each question, use this code as reference for solutions
\begin{solution}
    \begin{align*}
        \intertext{Momentum of the ball will change only along the normal($x$ direction).}
        \vec{J} &= \vec{p}_f-\vec{p}_i\\
        &= m\vec{v}_f-m\vec{v}_i\\
        &= m\left(\dfrac{3}{4}v_0\hat{i}\right)-m\left(v_0\hat{i}\right)\\
        &= -\dfrac{1}{4}mv_0\hat{i}\\
        &= -\dfrac{5}{4}mv_0\hat{i}
    \end{align*}
\end{solution}
Try not to use any derived formula if possible, go with fundamentals and basics. Also if possible use align* environment for solutions. You can add descriptive text in between using \intertext{} command. Solve every question and provide the solution as well. Don't separate the question and solution. Solution should be just below the question.
Try to use the \ans command at the end of the correct option, but check the answer for sure before marking. 

Please provide only the solution part of the LaTeX file, not the whole LaTeX file.
"""

answer = process_text("problem_18.tex", prompt, api_key, 1000)
print(answer)
