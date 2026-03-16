def game():
    num = 7
    attempts = 3
    
    print("\nYou have 3 attempts to guess the number.")
    
    while attempts:
        try:
            x = int(input("Guess a number between 1 to 10 : "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if x < 1 or x > 10:
            print("Out of range")
            continue
        
        if x == num:
            print("Correct guess.")
            return
        
        elif x > num:
            print("Too high")
        else:
            print("Too low")
        
        attempts -= 1
        print("Attempts left:", attempts)
    
    print("You are out of attempts.\nGame over.")

while True:
    game()
    
    choice = input("\nDo you want to play again? (y/n): ").lower()
    
    if choice == 'y':
        continue
    elif choice == 'n':
        print("Thanks for playing 🙂")
        break
    else:
        print("Invalid choice. Exiting game.")
        break
