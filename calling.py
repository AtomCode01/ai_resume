
from openai import OpenAI
import json
import os
from dotenv import load_dotenv

load_dotenv()

def generate_latex_from_json(json_path):

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    data_str = json.dumps(data, separators=(",", ":"))

    client = OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=os.getenv("NVIDIA_API_KEY")  # secure
    )

    prompt = f"""
Generate a professional resume in LaTeX format.

STRICT RULES:
- Output ONLY valid LaTeX
- Include \\documentclass{{article}}
- Include \\begin{{document}} and \\end{{document}}
- No explanations

DATA:
{data_str}
"""

    response = client.chat.completions.create(
        model="z-ai/glm5",
        messages=[
            {"role": "system", "content": "You generate clean LaTeX resumes."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=2000
    )

    return response.choices[0].message.content