def main():
    user_var_input = input(" Enter your variable : ")     
    print(convertVar(user_var_input))
    
def convertVar(user_var):
    text = ""
    for char in user_var:
        if char.isupper():
            text += "_"
            text += char.lower()
        else:
            text += char
    return text
            
main()