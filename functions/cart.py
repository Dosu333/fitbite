import streamlit as st
from google.genai import types
from db.cart import CART


def add_to_cart(item_name, quantity, item_price):
    cart = st.session_state.get("cart", CART)

    # Check if item already exists in cart
    for item in cart:
        if item["name"] == item_name:
            item["quantity"] += quantity
            item["total_price"] = item["quantity"] * item_price
            break
    else:
        cart.append({
            "name": item_name,
            "quantity": quantity,
            "unit_price": item_price,
            "total_price": quantity * item_price
        })
    return f"Added {quantity} x {item_name} to cart."


def view_cart():
    cart = st.session_state.get("cart", CART)
    if not cart:
        return "Your cart is empty."

    cart_details = "Your Cart:\n"
    total_amount = 0
    for item in cart:
        cart_details += f"""- {item['quantity']} x {item['name']} @
                        ₦{item['unit_price']} each
                        = ₦{item['total_price']}\n"""
        total_amount += item['total_price']
    cart_details += f"\nTotal Amount: ₦{total_amount}"
    return cart_details


def clear_cart():
    st.session_state["cart"] = []
    return "Cart has been cleared."


def remove_from_cart(item_name):
    cart = st.session_state.get("cart", CART)
    for item in cart:
        if item["name"] == item_name:
            cart.remove(item)
            return f"Removed {item_name} from cart."
    return f"{item_name} not found in cart."


def edit_cart(item_name, new_quantity):
    cart = st.session_state.get("cart", CART)
    for item in cart:
        if item["name"] == item_name:
            item["quantity"] = new_quantity
            item["total_price"] = new_quantity * item["unit_price"]
            return f"Updated {item_name} quantity to {new_quantity}."
    return f"{item_name} not found in cart."


schema_add_to_cart = types.FunctionDeclaration(
    name='add_to_cart',
    description="""Add an item to the user's cart with specified quantity.""",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            'item_name': types.Schema(
                type=types.Type.STRING,
                description="The name of the item to add to the cart."
            ),
            'quantity': types.Schema(
                type=types.Type.INTEGER,
                description="The quantity of the item to add."
            ),
            'item_price': types.Schema(
                type=types.Type.NUMBER,
                description="The price per unit of the item."
            ),
        }
    )
)

schema_view_cart = types.FunctionDeclaration(
    name='view_cart',
    description="View the current items in the user's cart.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={}
    )
)

schema_clear_cart = types.FunctionDeclaration(
    name='clear_cart',
    description="Clear all items from the user's cart.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={}
    )
)

schema_remove_from_cart = types.FunctionDeclaration(
    name='remove_from_cart',
    description="Remove a specific item from the user's cart.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            'item_name': types.Schema(
                type=types.Type.STRING,
                description="The name of the item to remove from the cart."
            ),
        }
    )
)

schema_edit_cart = types.FunctionDeclaration(
    name='edit_cart',
    description="Edit the quantity of a specific item in the user's cart.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            'item_name': types.Schema(
                type=types.Type.STRING,
                description="The name of the item to edit in the cart."
            ),
            'new_quantity': types.Schema(
                type=types.Type.INTEGER,
                description="The new quantity for the item."
            ),
        }
    )
)
