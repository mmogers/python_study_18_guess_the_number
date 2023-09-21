import random
print("\U0001F4A5	\U0001F4A5	\U0001F4A5 \033[1;32mGuess the Number\033[0;0m \U0001F4A5	\U0001F4A5	\U0001F4A5	")
print("Totally Random 1000000 to 1")

number = random.randint(1,1000000)
count = 0 
while True:
  count += 1
  print()
  print("Guess the number")
  guess = int(input(""))
  if guess < 0:
    print("Your guess is out of the required scope! Bye!")
    exit()
  elif guess > number:
    print("Lower")
    continue
  elif guess < number:
    print("Higher")
    continue
  else :
    print("\n\033[32mCorrect! You guessed the number from the", count, "guess!\033[0m")
    break
    