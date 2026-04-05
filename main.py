import random

MIN_VAL = 1
MAX_VAL = 100


def get_random_number(min_val, max_val):
    return random.randint(min_val, max_val)


def get_player_guess(min_val, max_val):
    while True:
        number = input('Enter a number: ')
        if number.isdigit():
            number = int(number)
            if min_val <= number <= max_val:
                return number
            else:
                print('Out of range')
        else:
            print('Error! Try again! Only numbers')


def play_game():
    count = 0
    pc_number = get_random_number(MIN_VAL, MAX_VAL)
    while True:
        user_number = get_player_guess(MIN_VAL, MAX_VAL)
        count += 1
        if user_number < pc_number:
            print('The number must be greater')
        elif user_number > pc_number:
            print('Nice try! But the number must be less')
        else:
            print('You win!')
            print(f'Your number of attempts {count}')
            break


def main():
    while True:
        play_game()
        answer = input('Do you wanna play again? y - yes, n - no: ').lower()
        if answer == 'y':
            print("Let's gooo")
        elif answer == 'n':
            print('It was fun! Thank you for the game!')
            break


if __name__ == '__main__':
    main()
