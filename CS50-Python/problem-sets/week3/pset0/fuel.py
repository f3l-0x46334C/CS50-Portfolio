def main():
    output = get_x_y(" Enter fuel fraction(X/Y) : ")
    print(check_fuel(output))


def check_fuel(output):
    text = None
    if output >= 99:
        text = "F"
    elif output <= 1:
        text = "E"
    else:
        text = f"{output}%"
    return text


def get_x_y(prompt) -> int:
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


main()
