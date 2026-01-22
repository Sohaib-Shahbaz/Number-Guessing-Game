import random

print("Welcome to Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
random_number = random.randint(1, 100)

difficulty = input("Choose a difficulty level, 'easy' or 'hard': ").lower()
lives = 5
if difficulty == "easy":
    lives += 5

print(f"You have {lives} lives.")
while lives > 0:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == random_number:
        print("You guessed right")
        break
    if guess < random_number:
        print("Higher")
        lives -= 1
        print(f"You have {lives} lives left")

    if guess > random_number:
        print("Lower")
        lives -= 1
        print(f"You have {lives} lives left")

if lives == 0:
    print("You lose, you ran out of lives.")

