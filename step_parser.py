# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain

# from langchain_community.llms import Ollama
# from langchain.llms import LlamaCpp

# def create_step_chain():
#     prompt = PromptTemplate(
#         input_variables=["sop_text"],
#         template="""
#         You are a helpful agent that converts SOP instructions into structured JSON steps.

#         SOP Text:
#         {sop_text}

#         Return JSON like:
#         [
#             {{"type": "browser", "action": "goto", "url": "..."}},
#             {{"type": "browser", "action": "click", "target": "..."}},
#             {{"type": "api", "action": "call", "endpoint": "...", "params": {{}} }}
#         ]
#         """
#     )
#     return LLMChain(
#         # llm=LlamaCpp(
#         #     model_path="models/llama3.2.gguf",  # Update path to your GGUF model
#         #     temperature=0,
#         #     n_ctx=4096,
#         #     verbose=True
#         # ),
        
#         llm = Ollama(model="llama3.2"),
#         prompt=prompt
#     )



# #######################
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from langchain_community.llms import Ollama
from langchain.llms import LlamaCpp

def create_step_chain():
    prompt = PromptTemplate(
        input_variables=["sop_text"],
        template="""
        You are an intelligent assistant that transforms Standard Operating Procedures (SOPs) into a structured list of executable JSON actions.

        Your task is to:
        1. Carefully read the SOP instructions and analyse whether the steps are for Browser or API call. it can either be one of the two.
        2. Try to be as accurate as possible in your analysis.
        3. For "browser" SOP, include actions like "goto", "click", "fill", etc., along with clear targets.
        4. For "api" SOP, extract the endpoint and relevant parameters from input.
        5. Make reasonable assumptions if exact details (like URLs or fields) are missing, and clearly label them as "assumed" in comments.

        SOP Text:
        {sop_text}

        Return JSON like:
        [
            {{"type": "browser", "action": "goto", "url": "..."}},
            {{"type": "browser", "action": "click", "target": "..."}},
            {{"type": "api", "action": "call", "endpoint": "...", "params": {{}} }}
        ]
        """
    )
    return LLMChain(
        # llm=LlamaCpp(
        #     model_path="models/llama3.2.gguf",  # Update path to your GGUF model
        #     temperature=0,
        #     n_ctx=4096,
        #     verbose=True
        # ),
        
        llm = Ollama(model="llama3.2"),
        prompt=prompt
    )
