import datetime

from sqlalchemy import Column, String, Float, BigInteger, Date, DateTime, Boolean
from sqlalchemy.orm import relationship

from .database import Base


class Budget(Base):
    __tablename__ = "budgets"

    uuid    = Column(String, primary_key=True, index=True)
    name    = Column(String, unique=True, index=True)
    created = Column(DateTime, default=datetime.datetime.utcnow)

    accounts          = relationship("Account", back_populates="budget")
    master_categories = relationship("MasterCategory", back_populates="budget")


class Account(Base):
    __tablename__ = "accounts"

    uuid        = Column(String, primary_key=True, index=True)
    name        = Column(String)
    description = Column(String)
    type        = Column(String)
    budget_type = Column(String)
    created     = Column(DateTime, default=datetime.datetime.utcnow)

    budget       = relationship("Budget", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account")


class MasterCategory(Base):
    __tablename__ = "master_category"

    uuid    = Column(String, primary_key=True, index=True)
    name    = Column(String, unique=True, index=True)
    created = Column(DateTime, default=datetime.datetime.utcnow)

    budget     = relationship("Budget", back_populates="master_categories")
    categories = relationship("Category", back_populates="master_category")


class Category(Base):
    __tablename__ = "category"

    uuid    = Column(String, primary_key=True, index=True)
    name    = Column(String, unique=True, index=True)
    amount  = Column(Float)
    created = Column(DateTime, default=datetime.datetime.utcnow)

    master_category = relationship("MasterCategory", back_populates="categories")
    Transactions    = relationship("Transaction", back_populates="category")


class Transaction(Base):
    __tablename__ = "transactions"

    id      = Column(BigInteger, primary_key=True, index=True)
    date    = Column(Date)
    payee   = Column(String)
    memo    = Column(String)
    outflow = Column(Float)
    inflow  = Column(Float)
    cleared = Column(Boolean, default=False)
    created = Column(DateTime, default=datetime.datetime.utcnow)

    account  = relationship("Account", back_populates="transactions")
    category = relationship("Category", back_populates="transactions")