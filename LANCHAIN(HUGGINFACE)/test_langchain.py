# Updated imports for langchain_classic
from langchain_classic.chains import LLMChain
from langchain_classic.prompts import PromptTemplate
from langchain_classic.llms import HuggingFacePipeline
from transformers import pipeline

# Load Hugging Face summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Wrap it in LangChain's LLM interface
llm = HuggingFacePipeline(pipeline=summarizer)

# Create a prompt template
prompt_template = """
Summarize the following text concisely:

{text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

# Create a LangChain chain
chain = LLMChain(llm=llm, prompt=prompt)

# Test with some text
text_to_summarize = """
LangChain is a framework for developing applications powered by language models.
It provides tools to build chains, agents, memory, and more.
Hugging Face offers a vast model hub and easy-to-use APIs for many NLP tasks.
"""
summary = chain.run(text=text_to_summarize)
print("Summary:\n", summary)
