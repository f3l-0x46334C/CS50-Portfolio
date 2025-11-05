def main():
    user_input = input(" - Enter math expression : ").strip()
    num1, op, num2 = user_input.split(" ")
    num1, num2 = float(num1), float(num2)
    
    result = calc(num1, op, num2)
    print(f"{result:.1f}")

def calc(x, op, y):
    match op:
        case "+":
            return x + y
        case "-":
            return x - y
        case "*":
            return x * y
        case "/":
            return x / y

main()
