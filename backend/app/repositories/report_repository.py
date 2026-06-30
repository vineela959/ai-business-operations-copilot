from sqlalchemy.orm import Session

from app.models.report import Report


class ReportRepository:

    @staticmethod
    def create(db: Session, title: str, content: str):
        report = Report(title=title, content=content)

        db.add(report)
        db.commit()
        db.refresh(report)

        return report

    @staticmethod
    def get_all(db: Session):
        return db.query(Report).order_by(Report.id.desc()).all()