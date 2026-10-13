import os

from dotenv import load_dotenv
from google import genai
from google.genai import types
from pinecone import Pinecone


load_dotenv()


# =========================================================
# Configuration
# =========================================================

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]
INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "rag-demo")

EMBEDDING_MODEL = "gemini-embedding-2"
EMBEDDING_DIMENSION = 384


# =========================================================
# Clients
# =========================================================

gemini_client = genai.Client(
    api_key=GEMINI_API_KEY
)

pinecone_client = Pinecone(
    api_key=PINECONE_API_KEY
)

index = pinecone_client.Index(INDEX_NAME)


def search_knowledge_base(query: str) -> str:
    """
    Search the Pinecone knowledge base for information relevant
    to the user's question.

    Args:
        query: The user's question or search query.

    Returns:
        Relevant information retrieved from Pinecone.
    """

    # ---------------------------------------------
    # Create query embedding
    # ---------------------------------------------

    response = gemini_client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=query,
        config=types.EmbedContentConfig(
            output_dimensionality=EMBEDDING_DIMENSION
        ),
    )

    query_embedding = response.embeddings[0].values

    # ---------------------------------------------
    # Search Pinecone
    # ---------------------------------------------

    search_result = index.query(
        vector=query_embedding,
        top_k=2,
        include_metadata=True,
    )

    # ---------------------------------------------
    # Build context
    # ---------------------------------------------

    if not search_result.matches:
        return "No relevant information was found."

    context_parts = []

    for match in search_result.matches:

        metadata = match.metadata or {}

        text = metadata.get("text", "")

        score = match.score

        context_parts.append(
            f"Similarity: {score:.4f}\n"
            f"Content: {text}"
        )

    return "\n\n---\n\n".join(context_parts)