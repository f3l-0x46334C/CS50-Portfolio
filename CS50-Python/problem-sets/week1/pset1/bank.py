def main():
    print(calc_reward())
   
def calc_reward() -> str:
    greetings_input = input(" Greet me : ").lower().strip()
    if greetings_input.startswith("hello"):
        reward = "$0"
    elif greetings_input.startswith("h"):
        reward = "$20"
    else:
        reward = "$100" 
        
    return reward

main()