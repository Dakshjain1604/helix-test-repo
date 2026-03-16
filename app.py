def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def broken_function(
    # SyntaxError: missing closing parenthesis
    print("this will cause CI to fail")
# another broken change
