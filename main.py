import random

MIN_VAL = 1
MAX_VAL = 100


def get_random_number(min_val, max_val):
    return random.randint(min_val, max_val)


def get_player_guess(min_val, max_val):
    while True:
        number = input("Guess a number (1–100): ")
        if number.isdigit():
            number = int(number)
            if min_val <= number <= max_val:
                return number
            else:
                print("Please enter a number between 1 and 100.")
        else:
            print("Invalid input. Enter a number.")


def play_game():
    count = 0
    pc_number = get_random_number(MIN_VAL, MAX_VAL)
    while True:
        user_number = get_player_guess(MIN_VAL, MAX_VAL)
        count += 1
        if user_number < pc_number:
            print("Too low. Go higher.")
        elif user_number > pc_number:
            print("Too high. Go lower.")
        else:
            print(f"You got it in {count} tries!")
            break


def main():
    while True:
        play_game()
        answer = input("Play again? (y / n): ").lower()
        if answer == 'y':
            print("Let's go.")
        elif answer == 'n':
            print("Good game. Come back anytime.")
            break


if __name__ == '__main__':
    main()
