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

## Definitions on In-Context Prompts
In-context learning technique
Explanation
Zero-shot learning
No example is provided in the prompt.
One-shot learning
One example is provided in the prompt.
Two-shot learning
Two examples are provided in the prompt.
Few-shot learning
A number of examples are provided in the prompt.
Chain of Thought (CoT)
A number of examples are provided in the prompt, and for each example, all the logical steps to achieve an objective are clearly explained.

## General Prompt Structure
 * Persona - You’re an experienced Large Language Model (LLM) developer and renowned speaker.
 * Context - You’ve been invited to give a keynote speech for a LLM event.
 * Instruction - Write the punch lines for the speech.
 * Input - Include the following facts:
            LLMs have become mainstream with the launch of ChatGPT in November 2022
            many popular LLMs and LLM based chatbots have been launched since then, such as LLAMA-2, Falcon180B, Bard.
            LLMs becoming as popular as search engines
            many companies want to integrate LLMs in their applications
 * Tone - Use a witty but entertaining tone.
 * Output - format Present the text in two paragraphs of 5 lines each.

 Using XML-like tags helps the LLM understand separation of terms:
 <Persona>...</Persona>

 