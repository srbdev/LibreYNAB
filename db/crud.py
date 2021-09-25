from sqlalchemy.orm import Session

from . import models, schemas


def get_budget(db: Session, uuid: str):
    return db.query(models.Budget).filter(models.Budget.uuid == uuid).first()


def get_budgets(db: Session):
    return db.query(models.Budget).all()


def create_budget(db: Session, budget: schemas.BudgetCreate):
    db_budget = models.Budget(uuid=budget.uuid, name=budget.name)
    db.add(db_budget)
    db.commit()
    db.refresh(db_budget)
    return db_budget


def delete_budget(db: Session, uuid: str):
    pass


def get_account(db: Session, uuid: str):
    return db.query(models.Account).filter(models.Account.uuid == uuid).first()


def get_accounts(db: Session):
    return db.query(models.Account).all()


def create_account(db: Session, account: schemas.Account):
    pass


def delete_account(db: Session, uuid: str):
    pass


def get_master_category(db: Session, uuid: str):
    return db.query(models.MasterCategory).filter(models.MasterCategory.uuid == uuid).first()


def get_master_categories(db: Session):
    return db.query(models.MasterCategory).all()


def create_master_category(db: Session, master_category: schemas.MasterCategory):
    pass


def delete_master_category(db: Session, uuid: str):
    pass


def get_category(db: Session, uuid: str):
    return db.query(models.Category).filter(models.Category.uuid == uuid).first()


def get_categories(db: Session):
    return db.query(models.Category).all()


def create_category(db: Session, category: schemas.Category):
    pass


def delete_category(db: Session, uuid: str):
    pass


def get_transaction(db: Session, uuid: str):
    return db.query(models.Transaction).filter(models.Transaction.uuid == uuid).first()


def get_transactions(db: Session):
    return db.query(models.Transaction).all()


def create_transaction(db: Session, category: schemas.Transaction):
    pass


def delete_transaction(db: Session, uuid: str):
    pass