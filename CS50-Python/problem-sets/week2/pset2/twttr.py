def main():
    user_input = input(" Enter your text : ")
    print(remove_chars(user_input))
    
def remove_chars(usr_str):
    text = ""
    words = ["A","E","I","O","U"]
    for char in usr_str:
        usr_str = usr_str.upper()
        if char.upper() not in words:
            text += char
        else:
            continue
    return text

main()