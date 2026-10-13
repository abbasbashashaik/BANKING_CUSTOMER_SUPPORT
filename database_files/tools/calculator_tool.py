def addition(a:int,b:int):
    """Use this tool only for addition of the given arguments."""
    return a+b
def multiplication(a:int,b:int):
    """Use this tool only for Multiplication of the given arguments."""
    return a*b
def Subtraction(a:int,b:int):
    """Use this tool only for Subtraction of the given arguments."""
    return a-b
def divide(a:int,b:int):
    """Use this tool only for Division of the given arguments."""
    return a+b
def calculate(expression:str)->str:
    """ Evaluate a mathematical expression.

    Args:
        expression: A mathematical expression such as
                    '5 + 4', '10 * 20', or '(10 + 5) * 3'."""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Calculation error: {e}"


