from sqlalchemy.orm import Session

from app.rag.embedder import generate_embedding
from app.repositories.rag_repository import RAGRepository
from app.services.ai_service import generate_ai_response


def answer_from_documents(question: str, db: Session) -> str:
    query_embedding = generate_embedding(question)

    chunks = RAGRepository.search_similar_chunks(
        db=db,
        query_embedding=query_embedding,
        limit=5
    )

    if not chunks:
        return "No relevant document content found."

    context = "\n\n".join([
        chunk.chunk_text
        for chunk in chunks
    ])

    prompt = f"""
You are a RAG Knowledge Agent.

Answer the user's question using only the document context below.

If the answer is not found in the context, say:
"I could not find that information in the uploaded documents."

Document Context:
{context}

User Question:
{question}
"""

    return generate_ai_response(prompt)