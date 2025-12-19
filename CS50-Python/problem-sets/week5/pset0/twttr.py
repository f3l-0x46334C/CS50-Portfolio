def main():
    user_input = input(" Enter your text : ")
    print(shorten(user_input))
    
def shorten(usr_str):
    text = ""
    words = ["A","E","I","o"] # 'O' to 'o' - Deleted 'U'
    for char in usr_str:
        # delete usr_str.upper()
        if char.upper() not in words:
            text += char
        else:
            continue
    return text

if __name__ == "__main__":
    main()