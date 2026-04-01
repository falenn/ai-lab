#!/usr/bin/env python
from langchain_openai import ChatOpenAI
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
  print("Demonstrating LangChain usange")

  # Instantiate ChatOpenAI and reference to the LLM
  llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY,
                   model_name="gpt-5-nano")
  
  prompt_input = """Write a concise message to remind users to be vigilant about phishing attacks."""
  
  print("invoking the llm")
  response = llm.invoke(prompt_input)
  print(response.content)
  
