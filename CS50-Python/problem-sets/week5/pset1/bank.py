def main():
    greetings_input = input("Greet me : ")
    print(f"${value(greetings_input)}")


def value(greeting) -> str:
    greeting = greeting.lower().strip()

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
