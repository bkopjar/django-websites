import random

number = random.randint(1,9)
guess = int(input("Input a number: "))

if guess > 9:
    print("Input a number between 1 and 9!")
elif guess == number:
    print("You guessed right")
elif guess < number:
    print("You guessed too low")
else:
    print("You guessed to high")
print("Random number is: %d" %number)
