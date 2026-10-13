from sqlalchemy import select
from sqlalchemy.orm import Session
from database_files.auth import current_user
from postgresql_files.connection import engine
from postgresql_files.models import Customer,Account,Transaction
from database_files.schemas import CustomerResponse,TransactionResponse,AccountResponse


def get_customer_details() -> dict:
    """
    Retrieve customer details using the customer's ID.

    Args:
        customer_id: The unique customer ID, for example c_1001.
   

    Returns:
        Customer information as a structured response.
    """

    with Session(engine) as session:

        cus_statement = select(Customer).where(
            Customer.customer_id == current_user.customer_id
        )

        customer = session.scalar(cus_statement)

        if customer is None:
            return {
                "success": False,
                "error": "you are not an authorised customer"
            }
        acc_stmt=select(Account).where(
            Account.customer_id==current_user
        )
    
        accounts=session.scalars(acc_stmt).all()



        acc_response=[AccountResponse(
                account_id=account.account_id,
                customer_id=account.customer_id,
                account_number=account.account_number,
                account_type=account.account_type,
                balance=str(account.balance),
                currency=account.currency,
                status=account.status,
                creditcard=account.creditcard,
            )
            for account in accounts
        ]
    


        response = CustomerResponse(
            customer_id=customer.customer_id,
            name=customer.name,
            email=customer.email,
            phone=customer.phone,
            address=customer.address,
            account=acc_response
        )

        return {
            "success": True,
            "customer": response.model_dump(),
        }

# from database_files.tools.customer_tools import get_customer_details
def get_account_transactions(account_id:str)->dict:
    """ This function call is used to get the transactions of the the account ids
    it will take the customer account id and do the filteration for account transaction history
    """
    with Session(engine) as con:
        stmt=select(Transaction).where(
            Transaction.account_id==account_id
        )
        transactions=con.scalars(stmt).all()
        if not transactions:
            return{
                "success":False,
                "error":"no transactions found"
            }
        trans_resp=[TransactionResponse(
            transaction_id=transaction.transaction_id,
            account_id=transaction.account_id,
            transaction_type=transaction.transaction_type,
            amount=str(transaction.amount),
            description=transaction.description,
            status=transaction.status,
            transaction_date=transaction.transaction_date,
        )
        for transaction in transactions
        ]

        acc_stmt=select(Account).where(
            Account.account_id==account_id
        )
        accounts=con.scalar(acc_stmt)
        resp=AccountResponse(
                account_id=accounts.account_id,
                customer_id=accounts.customer_id,
                account_number=accounts.account_number,
                account_type=accounts.account_type,
                balance=str(accounts.balance),
                currency=accounts.currency,
                status=accounts.status,
                creditcard=accounts.creditcard,
                transaction=trans_resp           
        )

        return{
            "success":True,
            "transactions":resp.model_dump()
        }

        
