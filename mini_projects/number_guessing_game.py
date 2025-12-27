#Program generates a random number
#User tries to guess the number
#Program tells if guess is too high or too low
#User gets limited attempts
#Program ends when guessed correctly or attempts finish

def game():
  num = 7
  attempts = 3
  print("You have 3 attempts to guess the number.")
  while attempts:
    x = int(input("Guess a number between 1 to 10 : "))
    if x == num:
      print("Correct guess.")
      return
    elif x > num and x <= 10:
      print("Too high")
    elif x < num and x <= 10:
      print("Too low")
    else:
      print("Out of range")
    attempts -= 1
    print("Attempts left:", attempts)
  print("You are out of attempts.\nGame over.")

game()
#Future improvement: handle invalid input using try-except and allow users to replay.
      


