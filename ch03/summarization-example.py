#!/usr/bin/env python
from openai import OpenAI
from ailab.util.config import Config

OPENAI_API_KEY = ""

def load_config():
  global OPENAI_API_KEY
  print(f"Starting the app")
  config = Config("./resources/config.yaml")
  OPENAI_API_KEY = config.config["openai"]["apikey"]
  print(f"loaded API Key: {OPENAI_API_KEY}")


if __name__ == "__main__":  
  load_config()

  client = OpenAI(api_key=OPENAI_API_KEY)
  with open("./resources/text/Moby-Dick.txt", 'r', encoding='utf-8') as f:
    moby_dick_book = f.read()
    
  