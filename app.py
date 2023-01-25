import os

import openai
import requests

from dotenv import load_dotenv
from os.path import join, dirname
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

openai.api_key = os.environ.get('OPENAI_API_KEY')

pretext = 'What does '
name = 'Cushman and Wakefield'
ending = ' do?'
whole_name = pretext+name+ending

def create_prompt(name):

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=name,
      temperature=0,
      max_tokens=100,
    )
    print(response.choices[0].text)

create_prompt(whole_name)
