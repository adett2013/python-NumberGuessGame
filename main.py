import random
print("Welcome to the number guessing game! You have to guess the random number between 1-5. Lets go!")
play = True
while (play):
  points = 0
  numbers = [1,2,3,4,5]
  randomnumber = random.choice(numbers)
  user_guess = int(input("Type your guess! "))
  if (randomnumber == user_guess):
    play = False
    print(f"You've guessed the correct number! Number: {randomnumber}")
    playagain = input("Type y to play again. Type n to quit. ")
    if (playagain == "yes" or playagain == "y"):
      play = True
    else:
      print("Thanks for playing my game. This means a lot to me!")
      print("Find more games on https://www.arne-dettmer.de")
      exit
  else:
    print(f"The random number was {randomnumber}")
    print("Try again. Note: The number has changed after your guess.")