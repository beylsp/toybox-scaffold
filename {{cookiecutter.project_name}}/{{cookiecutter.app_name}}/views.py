from flask import jsonify


# Foo
# ===
def hello(name):
    if not name:
        name = "world"
    return (
        jsonify(
            [{"greet": f"hello, {name}"}]
        ),
        200,
    )
