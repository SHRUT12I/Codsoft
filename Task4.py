import random
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_score = 0
    computer_score = 0

    print("Rock-Paper-Scissors Game")
    while True:
        print("\nOptions: rock, paper, scissors, or quit")
        user_choice = input("Enter your choice: ").lower()

        if user_choice == 'quit':
            break
        elif user_choice not in ('rock', 'paper', 'scissors'):
            print("Invalid choice. Please choose from rock, paper, scissors, or quit.")
            continue

        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()