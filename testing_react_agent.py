from crewai import Crew, Process, Agent, Task
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Qdrant
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders.markdown import UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools import BaseTool
# from crewai_tools.tools.rag import rag_tool
from crewai_tools import RagTool


# class RetrieverTool(rag_tool):
#     name: str = "sop_retriever"  # Type annotation for name
#     description: str = "Useful for fetching SOP steps for any merchant case or issue"  # Type annotation for description

#     def __init__(self, retriever):
#         super().__init__(retriever=retriever)  # Pass the retriever to RagTool constructor

#     def _run(self, query: str):
#         # Your custom logic for running the tool
#         docs = self.retriever.get_relevant_documents(query)
#         return "\n\n".join([doc.page_content for doc in docs])

#     def _arun(self, query: str):
#         raise NotImplementedError("Async not supported.")

# class SOPRetrieverTool(BaseTool):
#     name = "sop_retriever"
#     description = "Useful for fetching SOP steps for any merchant case or issue"

#     def __init__(self, retriever):
#         super().__init__()
#         self.retriever = retriever

#     def _run(self, query: str) -> str:
#         docs = self.retriever.get_relevant_documents(query)
#         return "\n".join([doc.page_content for doc in docs])


# Initialize local Ollama (llama3)
# ollama_llm = Ollama(model="llama3")

# os.environ["LLM_PROVIDER"] = "ollama"

# Setup HuggingFace Embeddings
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Qdrant config for local folder storage
qdrant = Qdrant.from_existing_collection(
    path="./qdrant_data",  # Local folder path for Qdrant
    collection_name="sops",
    embedding=embedding_model
)

# Function to load and embed markdown SOP files from ./sop folder
def ingest_sops():
    loader = DirectoryLoader(
        path="./sop",
        glob="**/*.md",
        loader_cls=UnstructuredMarkdownLoader
    )
    documents = loader.load()

    # Split documents
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)

    # Store to Qdrant
    qdrant.add_documents(chunks)

# Optional: Run this if you want to embed SOPs on first run
# ingest_sops()

# Custom tool wrapper around retriever
# class RetrieverTool(BaseTool):
#     name = "sop_retriever"
#     description = "Useful for fetching SOP steps for any merchant case or issue"

#     def __init__(self, retriever):
#         super().__init__()
#         self.retriever = retriever

#     def _run(self, query: str):
#         docs = self.retriever.get_relevant_documents(query)
#         return "\n\n".join([doc.page_content for doc in docs])

#     def _arun(self, query: str):
#         raise NotImplementedError("Async not supported.")

# # Create retriever tool from vector DB

# retriever_tool = RetrieverTool(retriever=qdrant.as_retriever())
# retriever_tool = RagTool(
#     retriever=qdrant.as_retriever(),
#     name="sop_retriever",
#     description="Useful for fetching SOP steps for any merchant case or issue",
#    embedding_model=embedding_model
# )

from pydantic import Field
from typing import Any

class RetrieverTool(BaseTool):
    name: str = "sop_retriever"
    description: str = "Useful for fetching SOP steps for any merchant case or issue"
    retriever: Any = Field(...)

    def _run(self, query: str):
        docs = self.retriever.get_relevant_documents(query)
        return "\n\n".join([doc.page_content for doc in docs])

    def _arun(self, query: str):
        raise NotImplementedError("Async not supported.")



# Create retriever tool from vector DB
retriever_tool = RetrieverTool(retriever=qdrant.as_retriever())


# Research Agent - retrieves SOP steps
research_agent = Agent(
    role='SOP Retriever',
    goal='Retrieve relevant SOPs for the given case',
    backstory='Expert in finding procedural documentation based on issue context.',
    verbose=True,
    allow_delegation=False,
    llm="ollama/llama3.2",  # Use local Ollama via LiteLLM
    tools=[retriever_tool]
)

# Execution Agent - extracts required info and decides what to do
exec_agent = Agent(
    role='Automation Executor',
    goal='Convert SOPs into actionable steps and trigger the right API calls',
    backstory='A seasoned engineer that understands the case context and automates resolution.',
    verbose=True,
    allow_delegation=False,
    llm="ollama/llama3.2"  # Use local Ollama via LiteLLM
)

# Sample task using the agents
# NOTE: We specify only the primary agent responsible for the task
# The Crew manages delegation and sequencing automatically

research_task = Task(
    description="Fetch relevant SOPs for: 'How to update recurring billing?'",
    expected_output="Relevant SOP steps for updating recurring billing.",
    agent=research_agent
)

exec_task = Task(
    description="Based on retrieved SOPs, derive API actions to resolve the issue.",
    expected_output="Step-by-step API actions to resolve the issue.",
    agent=exec_agent
)

crew = Crew(
    agents=[research_agent, exec_agent],
    tasks=[research_task, exec_task],
    verbose=True,
    process=Process.sequential
)

result = crew.kickoff()
print("\nFinal Result:\n", result)
