from fastembed import TextEmbedding

# Load the embedding model once
embedding_model = TextEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)


def generate_embedding(text: str):
    """
    Generate a 384-dimensional embedding for a text chunk.
    """
    embedding = next(embedding_model.embed([text]))
    return embedding.tolist()