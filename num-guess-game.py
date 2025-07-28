import random
def number_guessing_game():
    num=random.randint(1,100)
    attempts=0
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 to 100 .Try to guess it!")
    while True:
        guess=int(input("Enter your guess: "))
        attempts+=1
        if guess<num:
            print("Too low .Try again!")
        elif guess>num:
            print("Too high .Try again!")
        else:
            print(f"Congratulations! You guessed the {num} in {attempts} attempts, well done!  You win!")
            break
if __name__ == "__main__":
    number_guessing_game()