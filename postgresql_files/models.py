from datetime import datetime
from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Customer(Base):
    __tablename__ = "customers"

    customer_id: Mapped[str] = mapped_column(
        String(20),
        primary_key=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    phone: Mapped[str | None] = mapped_column(
        String(20),
    )

    address: Mapped[str | None] = mapped_column(
        String(255),
    )

    created_at: Mapped[datetime] = mapped_column()


class Account(Base):
    __tablename__ = "accounts"

    account_id: Mapped[str] = mapped_column(
        String(20),
        primary_key=True,
    )

    customer_id: Mapped[str] = mapped_column(
        ForeignKey("customers.customer_id"),
        nullable=False,
    )

    account_number: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    account_type: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    balance: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
    )

    currency: Mapped[str] = mapped_column(
        String(3),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column()
    creditcard: Mapped[str]=mapped_column(
        String(16)

    )


class Transaction(Base):
    __tablename__ = "transactions"

    transaction_id: Mapped[str] = mapped_column(
        String(20),
        primary_key=True,
    )

    account_id: Mapped[str] = mapped_column(
        ForeignKey("accounts.account_id"),
        nullable=False,
    )

    transaction_type: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    amount: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        String(255),
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    transaction_date: Mapped[datetime] = mapped_column()

