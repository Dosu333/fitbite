from functions.wallet import make_payment
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
