import openai
import os
import argparse
from ast import parse
from dotenv import load_dotenv


load_dotenv() # load variables defined in the .env file into current environment
openai.api_key = os.getenv("OPENAI_API_KEY")


PROMPT = """
You will receive a file's contents as text.
Generate a code review for the file.  Indicate what changes should be made to improve its style, performance, readability, and maintainability.  If there are any reputable libraries that could be introduced to improve the code, suggest them.  Be kind and constructive.  For each suggested change, include line numbers to which you are referring.
"""

filecontent = """
def mystery(x, y):
    return x ** y
"""

messages = [
    {"role": "system", "content": PROMPT},
    {"role": "user", "content": f"Code review the following file: {filecontent}"}
]

res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)
print(res.choices[0].message.content)
