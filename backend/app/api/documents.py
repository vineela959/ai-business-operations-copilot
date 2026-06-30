from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from pypdf import PdfReader
from docx import Document as DocxDocument
import io

from app.database.database import get_db
from app.repositories.document_repository import DocumentRepository
from app.repositories.document_chunk_repository import DocumentChunkRepository
from app.schemas.document import DocumentResponse
from app.rag.chunker import chunk_text
from app.rag.embedder import generate_embedding
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/documents", tags=["Documents"])


def extract_text_from_pdf(file_bytes: bytes) -> str:
    reader = PdfReader(io.BytesIO(file_bytes))
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text.strip()


def extract_text_from_docx(file_bytes: bytes) -> str:
    document = DocxDocument(io.BytesIO(file_bytes))
    text = "\n".join([paragraph.text for paragraph in document.paragraphs])
    return text.strip()


@router.post("/upload", response_model=DocumentResponse)
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    file_bytes = await file.read()

    if file.filename.endswith(".pdf"):
        content = extract_text_from_pdf(file_bytes)
    elif file.filename.endswith(".docx"):
        content = extract_text_from_docx(file_bytes)
    else:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are supported"
        )

    if not content:
        raise HTTPException(
            status_code=400,
            detail="No readable text found in document"
        )

    saved_document = DocumentRepository.create(
        db=db,
        filename=file.filename,
        content=content
    )

    chunks = chunk_text(content)

    chunks_with_embeddings = []

    for chunk in chunks:
        embedding = generate_embedding(chunk)

        chunks_with_embeddings.append({
            "chunk_text": chunk,
            "embedding": embedding
        })

    DocumentChunkRepository.create_many(
        db=db,
        document_id=saved_document.id,
        chunks_with_embeddings=chunks_with_embeddings
    )

    return saved_document


@router.get("/", response_model=list[DocumentResponse])
def get_documents(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return DocumentRepository.get_all(db)


@router.get("/chunks")
def get_chunks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    chunks = DocumentChunkRepository.get_all(db)

    return [
        {
            "id": chunk.id,
            "document_id": chunk.document_id,
            "chunk_text": chunk.chunk_text,
            "has_embedding": chunk.embedding is not None
        }
        for chunk in chunks
    ]

@router.delete("/{document_id}")
def delete_document(
    document_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    deleted = DocumentRepository.delete(db, document_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return {
        "message": "Document deleted successfully"
    }