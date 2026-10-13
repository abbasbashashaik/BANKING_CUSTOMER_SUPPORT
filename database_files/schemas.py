from datetime import datetime

from pydantic import BaseModel


class TransactionResponse(BaseModel):
    transaction_id: str
    account_id: str
    transaction_type: str
    amount: str
    description: str | None
    status: str
    transaction_date: datetime

class AccountResponse(BaseModel):
    account_id: str
    customer_id: str
    account_number: str
    account_type: str
    balance: str
    currency: str
    status: str
    transaction:list[TransactionResponse]=[]

class CustomerResponse(BaseModel):
    customer_id: str
    name: str
    email: str
    phone: str | None
    address: str | None
    account:list[AccountResponse]=[]

