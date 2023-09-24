from langchain.document_loaders import PyPDFLoader, OnlinePDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Pinecone
from sentence_transformers import SentenceTransformer
from langchain.chains.question_answering import load_qa_chain
import pinecone
import os

loader = PyPDFLoader("./sodapdf-converted.pdf")
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
docs = text_splitter.split_documents(data)

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY', 'be7268af-e963-4588-9c9f-392e5d759f9c')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV', 'gcp-starter')

embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

pinecone.init(
    api_key='be7268af-e963-4588-9c9f-392e5d759f9c',  # find at app.pinecone.io
    environment='gcp-starter'  # next to api key in console
)
index_name = "langchainpinecone" # put in the name of your pinecone index here

docsearch = Pinecone.from_texts([t.page_content for t in docs], embeddings, index_name="langchainpinecone")

query="what is the result of the case"
docs=docsearch.similarity_search(query)
docs

from langchain.llms import LlamaCpp
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from huggingface_hub import hf_hub_download
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

model_name_or_path = "TheBloke/CodeLlama-13B-Python-GGUF"
model_basename = "codellama-13b-python.Q5_K_M.gguf"
model_path = hf_hub_download(repo_id=model_name_or_path, filename=model_basename)

from langchain.llms import LlamaCpp
model_path = hf_hub_download(repo_id=model_name_or_path, filename=model_basename)
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
n_gpu_layers = 40
n_batch = 256

# Loading model,
llm = LlamaCpp(
    model_path = model_path,
    max_tokens=256,
    n_gpu_layers=n_gpu_layers,
    n_batch=n_batch,
    callback_manager=callback_manager,
    n_ctx=1024,
    verbose=True)

chain=load_qa_chain(llm, chain_type="stuff")

query="what is the result of the case"
docs=docsearch.similarity_search(query)
docs

chain.run(input_documents=docs, question=query)

from langchain.llms import HuggingFaceHub

chain=load_qa_chain(llm, chain_type="stuff")

query="what happened in 1951"
docs=docsearch.similarity_search(query)
chain.run(input_documents=docs, question=query)