from random import randint

def main():
    while True:
        level_str = input("Level: ")
        try:
            level = int(level_str)
            if level > 0:
                break
        except ValueError:
            pass

    target = randint(1, level)

    while True:
        guess_str = input("Guess: ")
        try:
            guess = int(guess_str)
            if guess <= 0:
                continue
        except ValueError:
            continue

        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
