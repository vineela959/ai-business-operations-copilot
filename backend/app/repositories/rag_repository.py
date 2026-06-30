from sqlalchemy.orm import Session
from app.models.document import DocumentChunk


class RAGRepository:

    @staticmethod
    def search_similar_chunks(db: Session, query_embedding: list[float], limit: int = 5):
        return (
            db.query(DocumentChunk)
            .order_by(DocumentChunk.embedding.l2_distance(query_embedding))
            .limit(limit)
            .all()
        )