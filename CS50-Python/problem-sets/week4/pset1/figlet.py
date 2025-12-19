from sys import argv, exit
from pyfiglet import Figlet
from random import choice

figlet = Figlet()
fig_fonts = figlet.getFonts()


def main():
    if len(argv) == 1:
        user_input = input("INPUT: ")
        figlet.setFont(font=choice(fig_fonts))
        print("OUTPUT:\n" + figlet.renderText(user_input))

    elif len(argv) == 3:
        if argv[1] in ("-f", "--font"):
            if argv[2] in fig_fonts:
                font = argv[2]
                figlet.setFont(font=font)
                user_input = input("INPUT: ")
                print("OUTPUT:\n" + figlet.renderText(user_input))
            else:
                exit(f"Font '{argv[2]}' not found")
        else:
            exit("Invalid command input")
    else:
        exit("Wrong arguments -> python figlet.py [ x ] [ y ] ")


main()
