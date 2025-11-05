from google.genai import types
import streamlit as st
from db.user import USERS
from db.cart import CART
from db.orders import ORDERS


def make_payment(amount, user_id):
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

    # Get the user's cart
    cart = st.session_state.get("cart", CART)
    orders = st.session_state.get("orders", ORDERS)
    if not cart:
        return {
            "status": "failure",
            "message": "Cart is empty. Add items before making a payment."
        }

    # Check if the user has sufficient balance
    balance = (
        st.session_state.wallet_balance
        if "wallet_balance" in st.session_state
        and st.session_state.user_id == user_id
        else user["wallet_balance"]
    )

    if balance < amount:
        return {
            "status": "failure",
            "message": f"Insufficient funds. Current balance: ₦{balance}",
        }

    # Deduct amount
    new_balance = balance - amount
    if ("wallet_balance" in st.session_state) and (
                                st.session_state.user_id == user_id):
        st.session_state.wallet_balance = new_balance
    else:
        user["wallet_balance"] = new_balance

    # Create an order from the cart
    order = {
        "user_id": user_id,
        "items": cart.copy(),
        "total_amount": sum(item["total_price"] for item in cart),
        "status": "paid",
    }
    orders.append(order)
    cart.clear()
    if st.session_state:
        st.session_state["orders"] = orders
        st.session_state["cart"] = cart

    return {
        "status": "success",
        "message": f"Payment of ₦{amount} successful.",
        "new_balance": new_balance,
    }


schema_make_payment = types.FunctionDeclaration(
    name='make_payment',
    description=""""
    Process payment for a user by deducting the specified amount from
    their wallet balance.
    """,
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            'amount': types.Schema(
                type=types.Type.NUMBER,
                description="""The amount to be deducted from
                            the user's wallet balance."""
            ),
        }
    )
)
