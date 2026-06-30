from sqlalchemy.orm import Session

from app.models.document import DocumentChunk


class DocumentChunkRepository:

    @staticmethod
    def create_many(db: Session, document_id: int, chunks_with_embeddings: list[dict]):
        db_chunks = [
            DocumentChunk(
                document_id=document_id,
                chunk_text=item["chunk_text"],
                embedding=item["embedding"]
            )
            for item in chunks_with_embeddings
        ]

        db.add_all(db_chunks)
        db.commit()

        return db_chunks

    @staticmethod
    def get_all(db: Session):
        return db.query(DocumentChunk).order_by(DocumentChunk.id.desc()).all()