import random
number_to_guess = random.randint(1, 100)

print("Welcome to the Number Guessing Game!🎯")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose difficulty (easy, medium, hard): ").lower()
if level == "easy":
    attempts = 7
elif level == "medium":
    attempts = 5
elif level == "hard":
    attempts = 3
print(f"You have {attempts} attempts to guess the number.\nGood luck!🍀")

for attempt in range(attempts):
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input! Please enter a number.❌")
        continue


    if guess == number_to_guess:
        print("Congratulations! You guessed the number correctly.✅")
        break
    elif guess < number_to_guess :
        print("Your guess is too low. Try again.📉")
    elif guess > number_to_guess:
        print("Your guess is too high. Try again.📈")
else:
    print(f" Game over! The correct number was {number_to_guess}❌")         