from sqlalchemy import select
from sqlalchemy.orm import Session
from postgresql_files.connection import engine
from postgresql_files.models import Account
from database_files.schemas import AccountResponse
from database_files.auth import current_user

def get_account_details(account_id:str)->dict:
    """ this tool is used for getting the account details of the current user"""

    with Session(engine) as con:
        stmt=select(Account).where(Account.account_id==account_id,
                                    Account.customer_id==current_user.customer_id
                                   )
        accounts=con.scalar(stmt)
        if accounts is None:
            return {
                "success":False,
                "error":"No accounts found ,you are not an authourised user"
                }
        response=AccountResponse(
            account_id=accounts.account_id,
            customer_id=accounts.customer_id,
            account_number=accounts.account_number,
            account_type=accounts.account_type,
            balance=str(accounts.balance),
            currency=accounts.currency,
            status=accounts.status,
            creditcard=accounts.creditcard,
        )
        return {
            "success":True,
            "Account":response.model_dump()
        }
    