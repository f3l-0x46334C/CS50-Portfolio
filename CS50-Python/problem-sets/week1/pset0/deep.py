def main():
    print("""
        “All right,” said the computer, and settled into silence again. The two men fidgeted. The tension was unbearable. “You’re really not going to like it,” observed Deep Thought. “Tell us!” “All right,” said Deep Thought. “The Answer to the Great Question…” “Yes…!” “Of Life, the Universe and Everything…” said Deep Thought. “Yes…!” “Is…” said Deep Thought, and paused. “Yes…!” “Is…” “Yes…!!!…?” “Forty-two,” said Deep Thought, with infinite majesty and calm.”\n — The Hitchhiker’s Guide to the Galaxy, Douglas Adams\n
    """)

    answer = input(" - Answer to the Great Question of Life, the Universe and Everything? ").lower().strip()

    # match case check
    match answer:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")
            
    # if/else check
    """
    if answer == "42" or answer == "forty-two" or answer == "forty two":
        print("Yes")
    else:
        print("No")
    """
    
main()