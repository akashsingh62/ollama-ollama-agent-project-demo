from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever


model = OllamaLLM(model="llama3")


template = """
You are an expert in answering questions about AI job listings and descriptions.

Here are some relevant job entries: {reviews}

Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


while True:
    print("\n\n-------------------------------")
    question = input("Ask your AI Job related question (q to quit): ")
    print("\n\n")
    if question.lower() == "q":
        break

    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews": reviews, "question": question})
    print(result)
