from sqlalchemy.orm import Session

from app.models.sale import Sale
from app.schemas.sale import SaleCreate


class SaleRepository:

    @staticmethod
    def get_all(db: Session):
        return db.query(Sale).order_by(Sale.id.desc()).all()

    @staticmethod
    def create(db: Session, sale: SaleCreate):
        db_sale = Sale(**sale.model_dump())

        db.add(db_sale)
        db.commit()
        db.refresh(db_sale)

        return db_sale