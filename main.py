from getpass import getpass as secretInput
print("\U0001F4A5	\U0001F4A5	\U0001F4A5 \033[1;32mGuess the Number\033[0;0m \U0001F4A5	\U0001F4A5	\U0001F4A5	")
print("Pick the number between 0 and 1000000")
number = int(secretInput(""))
if number < 0 or number > 1000000:
  print("The picked number is out of the required scope! Bye!")
  exit()

count = 0 
while True:
  count += 1
  print()
  print("Guess the number")
  guess = int(input(""))
  if guess < 0:
    print("The picked number is out of the required scope! Bye!")
    exit()
  elif guess > number:
    print("The number is lower")
    continue
  elif guess < number:
    print("The number is higher")
    continue
  else :
    print("\n\033[32mCorrect! You guessed the number from the", count, "guess!\033[0m")
    break