def main():
    userTextInput = input(" Enter Your Text : ")
    print(convert(userTextInput))
    
def convert(userText):
    return userText.replace(":)", "🙂").replace(":(", "🙁")

main()