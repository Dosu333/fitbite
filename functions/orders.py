import streamlit as st
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
