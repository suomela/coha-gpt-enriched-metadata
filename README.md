# COHA metadata enriched with LLMs



## Generation process

We used OpenAI API with the `gpt-4o-2024-08-06` model. Temperature was set to 0. We used the [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs/json-mode?api-mode=responses) API, with the output structure specification shown in [details/output.py](details/output.py).

The full system prompt is shown in [details/system-prompt.txt](details/system-prompt.txt); it included 50 manually annotated examples of input–output pairs. The user prompts looked similar to those shown in [details/example-prompt.txt](details/example-prompt.txt).
