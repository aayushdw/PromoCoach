"""
LlamaIndex with Google Gemini API and Local Embeddings - Basic Example
Prerequisites: pip install llama-index google-generativeai sentence-transformers
"""
import os
from dotenv import load_dotenv
# Load the .env file from the project root
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=dotenv_path)


from llama_index.core import VectorStoreIndex, Document, Settings
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import google.generativeai as genai


# Configure Google AI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ==============================================================================
# SETUP: Configure Gemini as the default LLM and embedding model
# ==============================================================================

def setup_gemini():
    """Configure LlamaIndex to use Gemini LLM and local embeddings"""
    
    # Set up local HuggingFace embeddings (runs on your machine, no API needed)
    embed_model = HuggingFaceEmbedding(
        model_name="BAAI/bge-small-en-v1.5"  # Fast, efficient, and accurate
    )
    
    # Set up Gemini LLM
    llm = Gemini(model_name="gemini-2.5-flash", api_key=os.getenv("GEMINI_API_KEY"))
    
    # Set as defaults
    Settings.llm = llm
    Settings.embed_model = embed_model

    print("embedding_model", embed_model.get_text_embedding_batch)
    
    print("Gemini LLM configured")
    print("Using local HuggingFace embeddings (BAAI/bge-small-en-v1.5)")

# ==============================================================================
# EXAMPLE: Basic Document Loading and Querying with Gemini
# ==============================================================================

def basic_example_gemini(document):
    """Load documents and query them using Gemini"""
    
    setup_gemini()
    
    # Create sample documents
    documents = [
        Document(text=f"{document}")
    ]
    
    # Build index (will use local embeddings)
    print("Building index...")
    index = VectorStoreIndex.from_documents(documents, show_progress=True)
    
    # Query the index (will use Gemini LLM for synthesis)
    print("\nQuerying index...")
    query_engine = index.as_query_engine()
    return query_engine
    # response = query_engine.query("What is LlamaIndex? Explain it in 3 sentences.")
    # print("\nResponse:", response)
    # print("\n")

# ==============================================================================
# Main execution
# ==============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("Basic Usage with Gemini")
    print("=" * 80)
    basic_example_gemini()