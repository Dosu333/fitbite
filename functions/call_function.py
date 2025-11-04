from functions.wallet import make_payment
from google.genai import types


def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"""Calling function:
            {function_call_part.name}({function_call_part.args})""")
    else:
        print(f"Calling function: {function_call_part.name}")

    result = ""
    if function_call_part.name == "make_payment":
        result = make_payment(**function_call_part.args)

    if result == "":
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={
                        "error": f"Unknown function: {function_call_part.name}"
                    },
                )
            ],
        )
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": result}
            )
        ]
    )
