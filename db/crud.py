from sqlalchemy.orm import Session

from . import models, schemas


def get_budget(db: Session, uuid: str):
    return db.query(models.Budget).filter(models.Budget.uuid == uuid).first()


def get_budgets(db: Session):
    return db.query(models.Budget).all()


def create_budget(db: Session, budget: schemas.Budget):
    pass