from src.helper import load_pdf_file, create_doc_chunks, download_hugging_face_embedding_model
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os 

# Get pinecone API Key from environment variables
load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

# Extract documents from PDF
documents = load_pdf_file(pdf_filepath='Data/')
# Split documents into chunks
doc_chunks = create_doc_chunks(documents)
# Download embedding model from Hugging Face
embed_model = download_hugging_face_embedding_model()

pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "medicalbot"

pc.create_index(
    name=index_name,
    dimension=384,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    )
)

# Embed each chunk and upsert the embeddings into the Pinecone index
docsearch = PineconeVectorStore.from_documents(
    documents=doc_chunks,
    index_name=index_name,
    embedding=embed_model
)

