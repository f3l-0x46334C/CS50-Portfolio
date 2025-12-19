import emoji


def main():
    user_input = input(" Text to emoji: ")
    print(emoji.emojize(user_input, language="alias"))


main()
