import openai
import os
import argparse
from dotenv import load_dotenv
from ast import parse


PROMPT = """
You will receive a file's contents as text.
Generate a code review for the file.  Indicate what changes should be made to improve its style, performance, readability, and maintainability.  If there are any reputable libraries that could be introduced to improve the code, suggest them.  Be kind and constructive.  For each suggested change, include line numbers to which you are referring
"""