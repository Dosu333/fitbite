from google.genai import types
from db.user import USERS


def make_payment(amount, user_id="user_001"):
    """
    Process payment for a user by deducting the specified amount from
    their wallet balance.

    Args:
        user_id (str): The unique identifier of the user making the payment.
        amount (float): The amount to be deducted from
                        the user's wallet balance.

    Returns:
        dict: A dictionary containing the status of the payment and
              updated wallet balance.
              Example: {"status": "success", "new_balance": 12000}
                       {"status": "failure", "message": "Insufficient funds"}
    """
    # Find the user by user_id
    user = next((user for user in USERS if user["id"] == user_id), None)

    if not user:
        return {"status": "failure", "message": "User not found"}

    # Check if the user has sufficient balance
    if user["wallet_balance"] < amount:
        return {"status": "failure", "message": "Insufficient funds"}

    # Deduct the amount from the user's wallet balance
    user["wallet_balance"] -= amount

    return {"status": "success", "new_balance": user["wallet_balance"]}


schema_make_payment = types.FunctionDeclaration(
    name='make_payment',
    description=""""
    Process payment for a user by deducting the specified amount from
    their wallet balance.
    """,
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            'user_id': types.Schema(
                type=types.Type.STRING,
                description="""The unique identifier of the
                            user making the payment."""
            ),
            'amount': types.Schema(
                type=types.Type.NUMBER,
                description="""The amount to be deducted from
                            the user's wallet balance."""
            ),
        }
    )
)
