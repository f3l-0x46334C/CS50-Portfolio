import random as ran

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        try_counter = 0
        while try_counter < 3:
            try:
                user_ans = int(input(f"{x} + {y} = "))
                if user_ans == (x + y):
                    score += 1
                    break
                else:
                    print("EEE")
                if try_counter == 2:
                    print(f"{x} + {y} = {x + y}")
            except ValueError:
                print("EEE")

            try_counter += 1

    print(f"Score : {score}")


def get_level():
    while True:
        try:
            level = int(input("Enter Level: "))
            if level in (1, 2, 3):
                return level
        except ValueError:
            print("ValueError")

def generate_integer(level):
    match level:
        case 1:
            return ran.randint(0, 9)
        case 2:
            return ran.randint(10, 99)
        case 3:
            return ran.randint(100, 999)
        case _:
            raise ValueError


if __name__ == "__main__":
    main()
