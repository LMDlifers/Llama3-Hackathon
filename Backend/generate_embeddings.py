# generate_embeddings.py
from llama_index import GPTListIndex, LLMPredictor, ServiceContext
from langchain import OpenAI

def generate_embeddings(data):
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="gpt-4"))
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
    documents = [Document(text) for text in data]
    index = GPTListIndex.from_documents(documents, service_context=service_context)
    return index
