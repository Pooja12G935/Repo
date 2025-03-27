import random

# Function to display the game images
def display_choice(choice):
    game_images = ["Rock", "Paper", "Scissors"]
    return game_images[choice]

# Main game function
def play_game():
    # Get user choice
    user_choice = int(input("Enter your choice (0 for Rock, 1 for Paper, 2 for Scissors): "))

    # Check for invalid input
    if user_choice < 0 or user_choice > 2:
        print("You have entered an invalid number. You lose!")
        return

    # Generate computer choice
    computer_choice = random.randint(0, 2)

    # Display choices
    print(f"You chose: {display_choice(user_choice)}")
    print(f"Computer chose: {display_choice(computer_choice)}")

    # Determine the outcome
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")

# Run the game
if __name__ == "__main__":
    play_game()
