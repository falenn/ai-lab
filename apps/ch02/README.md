# Ch02
## Intro to Prompts with LangChain
https://livebook.manning.com/book/ai-agents-and-applications/chapter-2#36


## Completions API
```
client.chat.completions.create(
    model=
    messages=
)
```
models refer to the OpenAI model you want to use.  These range from most accurate, slowest and expensive, to cheaper,faster and less-accurate:
GPT-5
GPT-5-mini
GPT-5-nano

messages are a list of messages, each with a role.  This structure is OpenAI convention for structureing conversational input.

* Reponses API is now OpenAI's preferred interface, particularly for agent-based workflows, but LangChain leverages the ChatOpenAI wrapper, which callse the Completions API.
* Completions API is also supported by many other open source LLMs.
