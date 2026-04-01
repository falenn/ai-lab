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
  
  prompt_input = """Write a concise message to remind users to be vigilant about phishing attacks."""
  response = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": prompt_input}
    ]
  )

  # Configured for a concise response
  print(f"AI Response: {response.choices[0].message.content}")