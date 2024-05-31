import random

target = random.randint(1,100)

while True:
    guess = int(input())

    if guess == target:
        print("You found it.")
        break
    elif guess < target:
        print("Go high.")
    elif guess > target:
        print("Go low.")