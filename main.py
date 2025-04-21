from config import *
from sop_loader import load_and_split_sops
from vector_store import build_vector_store ,load_vector_store 
from rag_chain import create_qa_chain
from step_parser import create_step_chain
import os
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def main():

    persist_path = "qdrant_data"
    collection_name = "sop_collection"

    if os.path.exists(persist_path):
        print("Loading existing vector store...")
        vector_db = load_vector_store(collection_name, persist_path)
    else:
        print("Loading and vectorizing SOPs...")
        documents = load_and_split_sops()
        print("Documents: ",    documents)
        vector_db = build_vector_store(documents, collection_name, persist_path)

    # print("Loading and vectorizing SOPs...")
    # documents = load_and_split_sops()
    # vector_db = build_vector_store(documents)

    print("Creating QA chain...")
    qa_chain = create_qa_chain(vector_db)
    
    ticket_input = "Please disable VPN and email access for empID 11223"
    # query = "What are the steps to disable VPN and email access for an employee?"
    # query = "Add the User ID W555555 to email distirubtion list 'MlOps."
    query = f'Terminate employee 999999 as the employee is not performing well.'
    # query = "Employee 999999 is being let go due to underperformance."
    # query = "The employee 999999 should be terminated due to bad behaviour."
    
    query = f'Update the name of merchant "abc tech" with id 12144 to "xyz Tech"'
    query = f'Enable Auto-Settlement for merchant  12144'

    print(f"\n--- Retrieved SOP Answer for query: {query} ---\n")
    result = qa_chain({"query": query})
    print(result["result"])

    print("\n--- Parsed Steps ---\n")
    step_chain = create_step_chain()
    steps = step_chain.run(sop_text=result["result"])
    print(steps)

    print("\n--- Execution Placeholder ---\n")
    print("Simulating action execution...")


if __name__ == "__main__":
    main()