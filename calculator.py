
# calculator.py

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b


OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}


def main():
    print("Simple Calculator")
    print("Operations:", ", ".join(OPERATIONS))

    op = input("Choose an operation: ").strip().lower()

    if op not in OPERATIONS:
        print("Unknown operation")
        return

    a = float(input("First number: "))
    b = float(input("Second number: "))

    print("Result:", OPERATIONS[op](a, b))


if __name__ == "__main__":
    main()
