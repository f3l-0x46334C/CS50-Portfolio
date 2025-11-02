def main():
    userTextInput = input(" Enter your text : ")
    print(playBackSpeed(userTextInput))
    
def playBackSpeed(text):
    return text.replace(" ", "...") 
      
main()