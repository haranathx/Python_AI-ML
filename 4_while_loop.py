# i=0

# while (i<=5):
#     print(i)
#     i=i+1


# i = int(input("Enter the number : "))

# while(i>=38):
#     i = int(input("Enter the number : "))
#     print(i)

# print("Loop is over")

# game guess the numbers

import random

number = random.randint(1, 100)
print(f"(Psst... the number is {number})")  # ← This reveals it immediately
guess = 0

while guess != number:
    guess = int(input("Guess the number (1-100): "))
    
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")

print("You got it!")
