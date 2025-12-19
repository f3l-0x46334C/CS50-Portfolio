def main():
    output = convert(" Enter fuel fraction(X/Y) : ")
    print(gauge(output))


def convert(prompt) -> int:
    while True:
        try:
            fraction = input(prompt)
            x, y = fraction.split("/")
            x, y = int(x), int(y)
            if x > y or x < 0:
                raise ValueError
            return int(round((x / y) * 100))
        except (ValueError, ZeroDivisionError):
            print(" ## WRONG INPUT or ZERO DIVISON ## ")


def gauge(output):
    text = None
    if output >= 99:
        text = "F"
    elif output <= 1:
        text = "E"
    else:
        text = f"{output}%"
    return text


if __name__ == "__main__":
    main()
