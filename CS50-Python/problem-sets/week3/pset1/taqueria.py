foods = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.75,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

def main():
    order()

def order():
    total = 0
    while True:
        try:
            item = input(" Item: ").title()
        except EOFError:
            print("")
            break

        if item in foods:
            total += foods[item]
            print(f"Total: ${total:.2f}")

main()