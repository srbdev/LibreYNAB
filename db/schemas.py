import datetime

from typing import List

from pydantic import BaseModel


class BudgetBase(BaseModel):
    uuid: str
    name: str


class AccountBase(BaseModel):
    uuid: str
    name: str
    type: str
    budget_type: str


class MasterCategoryBase(BaseModel):
    uuid: str
    name: str


class CategoryBase(BaseModel):
    uuid: str
    name: str
    amount: float


class TransactionBase(BaseModel):
    id: int
    date: datetime.date
    payee: str
    memo: str
    outflow: float
    inflow: float
    cleared: bool


class BudgetCreate(BudgetBase):
    pass


class Budget(BudgetBase):
    accounts: List[AccountBase] = []
    master_categories: List[MasterCategoryBase] = []

    class Config:
        orm_mode = True


class AccountCreate(AccountBase):
    pass


class Account(AccountBase):
    budget: BudgetBase
    Transactions: List[TransactionBase] = []

    class Config:
        orm_mode = True


class MasterCategoryCreate(MasterCategoryBase):
    pass


class MasterCategory(MasterCategoryBase):
    budget: BudgetBase
    categories: List[CategoryBase] = []

    class Config:
        orm_mode = True


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    master_category: MasterCategoryBase
    transactions: List[TransactionBase] = []

    class Config:
        orm_mode = True


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    account: AccountBase
    category: CategoryBase

    class Config:
        orm_mode = True