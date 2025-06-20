
# 🎯 Number Guessing Game Easy mode (Python)

Welcome to the **Number Guessing Game(easy)** built using Python!  
This is a beginner-friendly console game where the player has to guess a random number within a limited number of attempts.

---

## 📌 Features

- Random number between **1 and 100**
- **5 attempts** to guess the correct number
- Friendly feedback: 📉 Too low / 📈 Too high
- Error handling for non-number input
- Fun emojis for better readability 😄

---

## 🧠 How the Game Works

1. The computer randomly picks a number between 1 and 100.
2. The user has **5 chances**(medium) to guess it correctly.
3. After each guess:
   - If correct ➤ 🎉 You win!
   - If too low ➤ 📉 "Try again"
   - If too high ➤ 📈 "Try again"
4. If the player fails all 5 attempts ➤ ❌ Game over

---

## 🧾 Example Output

```
Welcome to the Number Guessing Game!🎯
I'm thinking of a number between 1 and 100.
Choose difficulty (easy, medium, hard): medium
You have 5 attempts to guess the number.
Good luck!🍀
Enter your guess: 5
Your guess is too low. Try again.📉

Enter your guess: 8
Your guess is too high. Try again.📈

...

Game over! The correct number was 7❌
```

---

## 🧑‍💻 Code Preview

```python
import random

number_to_guess = random.randint(1, 10)
attempts = 5

print("Welcome to the Number Guessing Game!🎯")
print("I'm thinking of a number between 1 and 10.")
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
    elif guess < number_to_guess:
        print("Your guess is too low. Try again.📉")
    elif guess > number_to_guess:
        print("Your guess is too high. Try again.📈")
else:
    print(f"Game over! The correct number was {number_to_guess}❌")
```

---

## 🛠️ How to Run

1. Install Python (if you haven't): [Download Python](https://www.python.org/downloads/)
2. Copy the code into a file named `guessing_game.py`
3. Run it in your terminal or code editor:

```bash
python guessing_game.py
```

---

## 📚 What You’ll Learn

- Using `random.randint()` for randomness
- Input handling and `try-except` error management
- Conditional logic with `if`, `elif`, `else`
- Loops and basic control flow
- User-friendly console output

---

## 🌟 Bonus Ideas to Improve

- Add **difficulty levels** (easy, medium, hard)
- Track and display **number of attempts used**
- Let user **restart** the game after finishing
- Add **score** tracking system

---

## 📬 Contributing

Want to improve this game or add features? Fork the repo and submit a pull request!  
Let’s help more beginners learn Python! 🐍
