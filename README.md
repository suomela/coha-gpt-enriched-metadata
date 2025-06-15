# COHA metadata enriched with LLMs

This is an enriched metadata file for the fiction section of the first version of the _Corpus of Historical American English_ (COHA; Davies 2010–), produced by Tanja Säily, Jukka Suomela, Florent Perek, Jimena Jiménez Real and Turo Vartiainen. The LLM-generated metadata includes genre, target audience, publication year, author gender, and author year of birth. Note that this is a pilot version, and the genre metadata in particular targets novels and is only about 70% accurate. The metadata on author gender, on the other hand, is >95% accurate. For more information, see Säily et al. (2025).

## Original metadata

We used a metadata file entitled `cohaTexts.xls` downloaded from the COHA website.

## Generation process

We used OpenAI API with the `gpt-4o-2024-08-06` model. Temperature was set to 0. We used the [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs/json-mode?api-mode=responses) API, with the output structure specification shown in [details/output.py](details/output.py).

The full system prompt is shown in [details/system-prompt.txt](details/system-prompt.txt); it included 50 manually annotated examples of input–output pairs. The user prompts looked similar to those shown in [details/example-prompt.txt](details/example-prompt.txt).

## References

Davies, Mark. 2010–. _The Corpus of Historical American English_: 400 million words, 1810–2009. https://www.english-corpora.org/coha/

Säily, Tanja, Jukka Suomela, Florent Perek, Jimena Jiménez Real & Turo Vartiainen. 2025. Using large language models to enrich corpus metadata: The case of novels in the _Corpus of Historical American English_. 46th Annual Conference of the International Computer Archive of Modern and Medieval English (ICAME 46), Vilnius, Lithuania, June 2025. https://docs.google.com/presentation/d/1_0jfmRFuflZ1h2HWfU2inZYHA6i4cO8mf5nVlFiXE0o/edit?usp=sharing
