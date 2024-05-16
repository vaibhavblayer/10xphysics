import base64
import requests
import os
import re
from rich.console import Console
import pyperclip

api_key = os.environ["OPENAI_API_KEY"]


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


prompt_subjective = """
Extract Questions from Image and Format in LaTeX
Please analyze the image provided and extract any questions present in the text. Format the questions in LaTeX format. If there are any diagrams present, please create only the TikZ environment with a node "Diagram" only, put it within the center environment. Please provide only the enumerated part of the LaTeX file, not the whole LaTeX file.
"""

prompt_mcq = """
Please analyze the image provided and extract any questions present in the text. Format the questions in LaTeX format. If there are any diagrams present, please create only the TikZ environment with a node "Diagram" only, put it within the center environment. If there are any multiple-choice questions, please put the options in a tasks environment. Please provide only the enumerated part of the LaTeX file, not the whole LaTeX file.
"""

prompt_match = """
Please analyze the image provided and extract any questions present in the text. Format the questions in LaTeX format. If there are any diagrams present, please create only the TikZ environment with a node "Diagram" only. If there are any multiple-choice questions, please put the options in a tasks environment. If there are any match-type questions, please create a table use this code as reference 
\begin{center}
    \renewcommand{\arraystretch}{2}
    \begin{table}[h]
        \centering
        \begin{tabular}{p{0.25cm}p{7cm}|p{0.25cm}p{6cm}}
        \hline
        & Column I & &Column II \\
        \hline
        (a)& When the velocity of $3\kg$ block is $\dfrac{2}{3}\mps$ & (p) &Velocity of center of mass is $\dfrac{2}{3}\mps$\\
        (b)& When the velocity of $6\kg$ block is $\dfrac{2}{3}\mps$ & (q) &Deformation of the spring is zero\\
        (c)& When the speed of $3\kg$ block is minimum  & (r) &Deformation of the spring is maximum\\
        (d)& When the speed of $6\kg$ block is maximum & (s) &Both the blocks are at rest with respect to each other\\
        \hline
        \end{tabular}
    \end{table}
\end{center}
Please provide only the enumerated part of the LaTeX file, not the whole LaTeX file.
"""


prompt_comprehension = """
Please analyze the image provided and extract any questions present in the text. Format the questions in LaTeX format. If there are any diagrams present in any type of question, please create only the TikZ environment with a node "Diagram" only in center environment. If there are any multiple-choice questions, please put the options in a tasks environment. If there are any comprehension type questions, use this code as reference  
\begin{center}
    \textsc{Comprehension-II}
\end{center}
A uniform wire frame of linear mass density $\lambda$ having three sides each of length $2a$ is kept on a smooth horizontal surface. An impulse $J$ is applied at one end as shown in the figure. $P$ is the midpoint of $AB$. Now answer the following questions. 
\begin{center}
    \begin{tikzpicture}
        \pic[rotate=180] at (0, 0) {frame=3cm};
    \end{tikzpicture}
\end{center} 
\begin{enumerate}
    \item The angular velocity of the system just after the impulse is
        \begin{tasks}(4)
            \task $\dfrac{3J}{22\lambda a^2}$\ans
            \task $\dfrac{J}{22\lambda a^2}$
            \task $\dfrac{2J}{22\lambda a^2}$
            \task $\dfrac{4J}{22\lambda a^2}$
        \end{tasks}

    \item The velocity of point $P$ just after the impulse is
        \begin{tasks}(4)
            \task $\dfrac{J}{\lambda a}\hat{j}$
            \task $\dfrac{J}{6\lambda a}\hat{j}$
            \task $\dfrac{J}{\lambda a}\left(\dfrac{2}{11}\hat{i} + \dfrac{1}{6}\hat{j}\right)$
            \task $\dfrac{J}{\lambda a}\left(\dfrac{1}{11}\hat{i} + \dfrac{1}{6}\hat{j}\right)$\ans
        \end{tasks} 
\end{enumerate}
Please provide only the comprehension and enumerate part of the LaTeX file, not the whole LaTeX file.
"""

prompt = prompt_mcq


def create_image_dicts(image_names):
    image_dicts = []
    for image_name in image_names:
        base64_image = encode_image(image_name)
        image_dict = {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/png;base64,{base64_image}"
            }
        }
        image_dicts.append(image_dict)
    return image_dicts


image_names = ["main-21.png", "main-21-C.png"]
image_dicts = create_image_dicts(image_names)


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
                *image_dicts
            ]
        }
    ],
    "max_tokens": 3000
}


response = requests.post(
    "https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

message = response.json()["choices"][0]["message"]["content"]
pattern = r"```latex(.*?)```"
matches = re.findall(pattern, message, re.DOTALL)


pyperclip.copy(matches[0])


Console().print(
    message,
    style="deep_pink3"
)
