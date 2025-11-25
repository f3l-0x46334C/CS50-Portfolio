grocery_dict = {}


def main():
    while True:
        try:
            user_item = input().strip().upper()
            if user_item == "":
                continue
            adding_dict(user_item)
        except EOFError:
            print()
            sorting_dict()
            break


def adding_dict(item):
    grocery_dict[item] = grocery_dict.get(item , 0) + 1


def sorting_dict():
    for key in sorted(grocery_dict.keys()):
        print(f"{grocery_dict[key]} {key}")


main()
