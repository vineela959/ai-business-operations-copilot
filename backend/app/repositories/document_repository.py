from sqlalchemy.orm import Session

from app.models.document import Document, DocumentChunk


class DocumentRepository:

    @staticmethod
    def create(db: Session, filename: str, content: str):
        document = Document(
            filename=filename,
            content=content
        )

        db.add(document)
        db.commit()
        db.refresh(document)

        return document

    @staticmethod
    def get_all(db: Session):
        return (
            db.query(Document)
            .order_by(Document.created_at.desc())
            .all()
        )

    @staticmethod
    def get_by_id(db: Session, document_id: int):
        return (
            db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )

    @staticmethod
    def delete(db: Session, document_id: int):
        document = (
            db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )

        if not document:
            return False

        db.query(DocumentChunk).filter(
            DocumentChunk.document_id == document_id
        ).delete()

        db.delete(document)
        db.commit()

        return True