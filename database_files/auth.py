class AuthenticatedUser:
    def __init__(self,customer_id:str):
        self.customer_id=customer_id
current_user = AuthenticatedUser(
    customer_id="c_1002"
)