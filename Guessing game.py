import random

number = random.randint(1,20)

for i in range(4):
    print(f"input your {i + 1} guess")
    our_guess = int(input())

    if our_guess == number:
      print("YES, You win!")
      break
    elif our_guess > number:
      print("Your guess is higher!")
    elif our_guess < number:
      print("Your guess is lower")

    if i == 3:
      print("You LOOSE!!!")