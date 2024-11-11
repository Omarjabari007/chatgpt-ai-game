import random
import time
import sys

# List of animals categorized by types
animals = {
    "Mammals": [
        {"name": "Lion", "clue": "I am the king of the jungle."},
        {"name": "Elephant", "clue": "I have a long trunk and big ears."},
        {"name": "Kangaroo", "clue": "I carry my babies in a pouch."},
        {
            "name": "Giraffe",
            "clue": "I have a long neck and eat leaves from tall trees.",
        },
        {"name": "Bear", "clue": "I hibernate during the winter."},
    ],
    "Birds": [
        {"name": "Penguin", "clue": "I am a bird that cannot fly, but I can swim."},
        {
            "name": "Eagle",
            "clue": "I am known for my keen eyesight and powerful wings.",
        },
        {
            "name": "Ostrich",
            "clue": "I am the largest bird and can't fly, but I can run fast.",
        },
        {
            "name": "Parrot",
            "clue": "I am known for mimicking sounds and have colorful feathers.",
        },
    ],
    "Sea Animals": [
        {
            "name": "Shark",
            "clue": "I am a large fish, known as a predator of the ocean.",
        },
        {"name": "Octopus", "clue": "I have eight arms and can change color."},
        {"name": "Whale", "clue": "I am the largest animal on earth."},
        {
            "name": "Dolphin",
            "clue": "I am known for my intelligence and playful behavior.",
        },
    ],
}

# Game settings
score = 0
max_level = 5
attempts = 3
time_limit = 15  # Time limit per question in seconds
level = 1
high_score = 0


# Function to print the welcome screen
def print_welcome_screen():
    print("Welcome to the Animal Guessing Game!")
    print("In this game, you will guess animals based on clues.")
    print("You can choose different animal categories and difficulty levels.")
    print("You have a limited time to answer each question.")
    print("Good luck!\n")


# Function to display the main menu
def main_menu():
    print("Main Menu:")
    print("1. Start Game")
    print("2. High Scores")
    print("3. Help")
    print("4. Quit")
    choice = input("Choose an option: ")
    if choice == "1":
        start_game()
    elif choice == "2":
        show_high_scores()
    elif choice == "3":
        show_help()
    elif choice == "4":
        sys.exit()
    else:
        print("Invalid choice. Please try again.")
        main_menu()


# Function to show high scores
def show_high_scores():
    global high_score
    print(f"\nHigh Score: {high_score}")
    main_menu()


# Function to show help screen
def show_help():
    print("\nHelp:")
    print("1. The game will give you a clue about an animal.")
    print("2. You will have a limited amount of time to guess the animal.")
    print("3. Each correct answer earns you a point.")
    print("4. You can choose different animal categories and difficulty levels.\n")
    main_menu()


# Function to start the game
def start_game():
    global score, level, attempts, time_limit, high_score
    print_welcome_screen()

    print("Choose an animal category:")
    print("1. Mammals")
    print("2. Birds")
    print("3. Sea Animals")
    category_choice = input("Choose an option: ")

    if category_choice == "1":
        category = "Mammals"
    elif category_choice == "2":
        category = "Birds"
    elif category_choice == "3":
        category = "Sea Animals"
    else:
        print("Invalid category. Defaulting to Mammals.")
        category = "Mammals"

    print("\nChoose difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    difficulty_choice = input("Choose an option: ")

    if difficulty_choice == "1":
        attempts = 5
        time_limit = 20
    elif difficulty_choice == "2":
        attempts = 3
        time_limit = 15
    elif difficulty_choice == "3":
        attempts = 2
        time_limit = 10
    else:
        print("Invalid difficulty. Defaulting to Medium.")
        attempts = 3
        time_limit = 15

    play_level(category)


# Function to play a single level
def play_level(category):
    global score, level, attempts, time_limit, high_score
    print(f"\nLevel {level}:")
    animal = random.choice(animals[category])
    print(f"Clue: {animal['clue']}")

    correct_answer = animal["name"].lower()
    attempts_left = attempts

    print(f"You have {time_limit} seconds to answer.")
    start_time = time.time()

    while attempts_left > 0:
        guess = input(
            f"Guess the animal (You have {attempts_left} attempts left): "
        ).lower()

        elapsed_time = time.time() - start_time
        if elapsed_time > time_limit:
            print(f"Time's up! The correct answer was: {animal['name']}")
            break

        if guess == correct_answer:
            print("Correct! You earned a point!")
            score += 1
            break
        else:
            attempts_left -= 1
            if attempts_left > 0:
                print(f"Incorrect! You have {attempts_left} attempts left.")
            else:
                print(f"Sorry! The correct answer was: {animal['name']}")

    level += 1
    if level <= max_level:
        play_level(category)
    else:
        end_game()


# Function to end the game and display the score
def end_game():
    global score, level, high_score
    print(f"\nGame Over! Your final score is {score}/{max_level}.")
    if score > high_score:
        high_score = score
        print("Congratulations! You set a new high score!")
    elif score == high_score:
        print("You tied with the high score!")
    elif score >= max_level // 2:
        print("Good job! You did well!")
    else:
        print("Better luck next time!")

    print("\nWould you like to play again? (y/n): ")
    play_again = input().lower()
    if play_again == "y":
        score = 0
        level = 1
        start_game()
    else:
        main_menu()


# Main entry point of the game
if __name__ == "__main__":
    main_menu()
