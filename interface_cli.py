from config import *
from sop_loader import load_and_split_sops
from vector_store import build_vector_store, load_vector_store
from rag_chain import create_qa_chain
from step_parser import create_step_chain
from executor import execute_steps

def run_pipeline():
    documents = load_and_split_sops()
    vector_db = build_vector_store(documents)

    qa_chain = create_qa_chain(vector_db)
    step_chain = create_step_chain()

    ticket_input = input("\nEnter ticket description:\n> ")
    query = f"What are the steps to resolve this ticket: {ticket_input}"

    result = qa_chain({"query": query})
    print("\n--- Retrieved SOP Answer ---\n")
    print(result["result"])

    steps = step_chain.run(sop_text=result["result"])
    print("\n--- Parsed JSON Steps ---\n")
    print(steps)

    print("\n--- Simulating Execution ---\n")
    execute_steps(steps)

if __name__ == "__main__":
    run_pipeline()
