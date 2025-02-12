from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load data from PDF file
def load_pdf_file(pdf_filepath):
    loader = DirectoryLoader(pdf_filepath, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents


# Split the documents into chunk
def create_doc_chunks(docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    doc_chunks = text_splitter.split_documents(docs)
    return doc_chunks


# Download embedding model from Hugging Face
def download_hugging_face_embedding_model():
    embed_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    return embed_model