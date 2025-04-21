# from langchain.document_loaders import DirectoryLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter

# def load_and_split_sops(path="./sops", file_type="*.md"):
#     loader = DirectoryLoader(path, glob=file_type)
#     documents = loader.load()

#     # Print out the original Document objects for debugging
#     # print("SOP Loader: Documents 2 : ", [doc.page_content for doc in documents])
    
#     # Create a text splitter (splitting based on character length)
#     splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    
#     # Split the documents into smaller chunks (pass the Document objects as they are)
#     x = splitter.split_documents(documents)
#     print(x)
#     return x

# load_and_split_sops()


import re
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

def load_and_split_sops(path="./sops", file_type="*.md"):
    loader = DirectoryLoader(path, glob=file_type)
    documents = loader.load()

    # Extract SOPs from the document (split by a header pattern like "SOP: ")
    sop_texts = []
    for doc in documents:
        content = doc.page_content
        
        # Define a regex pattern to match SOPs (assuming "SOP: " followed by the SOP title)
        sop_pattern = r"(SOP: [^\n]+[\n]+)(.*?)(?=SOP: |$)"
        
        # Find all SOPs
        sop_matches = re.findall(sop_pattern, content, flags=re.DOTALL)
        
        # Each SOP is extracted as a document
        sop_texts.extend([match[1].strip() for match in sop_matches])

    # Now we need to split large SOPs into chunks (if they exceed the chunk_size)
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

    # Create Document objects for each SOP text
    sop_documents = [Document(page_content=sop_text) for sop_text in sop_texts]
    
    # Split each SOP into smaller chunks (if needed)
    return splitter.split_documents(sop_documents)

# Run the loader and splitter
# print("Loading and vectorizing SOPs...\n", load_and_split_sops())

