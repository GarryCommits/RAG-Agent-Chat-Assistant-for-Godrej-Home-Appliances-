from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """
Your are an expert in answering questions about a Smart home applicances

Here are some revelant reviews: {reviews}

Here is the question to answer: {question}"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n--------------------------------")
    question = input("Ask your question (q to quit): ")
    print("\n\n")
    if question == "q":
        break

    reviews = retriever.invoke(question)
    result = chain.invoke({
        "question": question,
        "reviews": "\n".join(review.page_content for review in reviews),
    })
    print(result)
