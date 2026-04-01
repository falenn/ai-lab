#!/usr/bin/env python
from openai import OpenAI
from ailab.util.config import Config
from langchain_openai import ChatOpenAI

OPENAI_API_KEY = ""

def load_config():
  global OPENAI_API_KEY
  print(f"Starting the app")
  config = Config("./resources/config.yaml")
  OPENAI_API_KEY = config.config["openai"]["apikey"]
  print(f"loaded API Key: {OPENAI_API_KEY}")


if __name__ == "__main__":  
  load_config()
  llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY,
                 model_name="gpt-5-mini")
  
  prompt_input = """Classify the following numbers as Abra, Kadabra 
    or Abra Kadabra:

    3, 4, 5, 7, 8, 10, 11, 13, 35

    Examples: 
    6 // not divisible by 5, not divisible by 7 // None
    15 // divisible by 5, not divisible by 7 // Abra
    12 // not divisible by 5, not divisible by 7 // None
    21 // not divisible by 5, divisible by 7 // Kadabra
    70 // divisible by 5, divisible by 7 // Abra Kadabra
    """

  response = llm.invoke(prompt_input)
  print(response.content)