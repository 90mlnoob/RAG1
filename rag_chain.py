# from langchain.llms import LlamaCpp
# from langchain.chains import RetrievalQA

# from langchain_community.llms import LlamaCpp
from langchain_community.llms import Ollama
# from langchain_community.chains import RetrievalQA
from langchain.chains import RetrievalQA


def create_qa_chain(vector_db):
    retriever = vector_db.as_retriever()
    # llm = LlamaCpp(
    #     # model_path="models/llama3.2.gguf",  # Update with your actual model path
    #     model_path = "C:\\Users\\Saurav Suman\\AppData\\Local\\Programs\\Ollama\\llama3.2.gguf",
    #     temperature=0,
    #     n_ctx=4096,
    #     verbose=True
    # )
    
    llm = Ollama(model="llama3.2")
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

# a = create_qa_chain()
# llm = LlamaCpp(
#         # model_path="models/llama3.2.gguf",  # Update with your actual model path
#         model_path = "C:\\Users\\Saurav Suman\\AppData\\Local\\Programs\\Ollama\\llama3.2",
#         temperature=0,
#         n_ctx=4096,
#         verbose=True
    # )
    # from langchain_community.llms import Ollama

if __name__ == "__main__":
    
    from langchain.prompts import PromptTemplate
    from langchain.chains import LLMChain

    llm = Ollama(model="llama3.2")

    prompt = PromptTemplate.from_template("Translate '{text}' to French.")
    chain = LLMChain(llm=llm, prompt=prompt)

    result = chain.run("I love programming.")
    print(result)
    