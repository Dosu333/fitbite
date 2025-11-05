from functions.wallet import make_payment
from functions.cart import (add_to_cart, view_cart, clear_cart,
                            remove_from_cart, edit_cart)
from functions.orders import get_orders
from google.genai import types


def call_function(function_call_part, verbose=True, user_id=None):
    if verbose:
        print(f"""Calling function:
            {function_call_part.name}({function_call_part.args})""")
    else:
        print(f"Calling function: {function_call_part.name}")

    result = ""
    if function_call_part.name == "make_payment":
        result = make_payment(user_id=user_id, **function_call_part.args)
    elif function_call_part.name == "add_to_cart":
        result = add_to_cart(**function_call_part.args)
    elif function_call_part.name == "view_cart":
        result = view_cart()
    elif function_call_part.name == "clear_cart":
        result = clear_cart()
    elif function_call_part.name == "remove_from_cart":
        result = remove_from_cart(**function_call_part.args)
    elif function_call_part.name == "edit_cart":
        result = edit_cart(**function_call_part.args)
    elif function_call_part.name == "get_orders":
        result = get_orders(user_id=user_id)
    else:
        result = {"status": "failure", "message": "Function not found"}

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response=result
            )
        ]
    )
