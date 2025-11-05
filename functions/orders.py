import streamlit as st
from google.genai import types
from db.orders import ORDERS


def get_orders(user_id):
    """
    Retrieve the list of orders for the current user.

    Returns:
        list: A list of orders associated with the current user.
    """
    orders = st.session_state.get("orders", ORDERS)
    user_orders = [order for order in orders if order["user_id"] == user_id]
    return user_orders


schema_get_orders = types.FunctionDeclaration(
    name='get_orders',
    description="Retrieve the list of orders for the current user.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            'user_id': types.Schema(
                type=types.Type.STRING,
                description="The unique identifier of the user."
            ),
        }
    )
)
