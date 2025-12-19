from sys import exit
import inflect

names = []
p = inflect.engine()


def main():
    while True:
        try:
            user_name = input("Name : ")
            names.append(user_name)
        except EOFError:
            """
            # without module
            print("\nAdieu, adieu, to ", end="")
            for i, name in enumerate(names):
                if i == len(names) - 1:
                    print("and " + name, end="")
                else:
                    print(name + ", ", end="")
            """
            print("\nAdieu, adieu, to", p.join(names))
            exit()


main()
