# 🎮 Rock-Paper-Scissors Game
# 🧠 Created by Malini M

import random

def get_user_choice():
    print("\nChoose one:")
    print("🪨 Rock")
    print("📄 Paper")
    print("✂️ Scissors")
    choice = input("👉 Enter rock, paper, or scissors: ").lower()
    if choice in ["rock", "paper", "scissors"]:
        return choice
    else:
        print("🚫 Invalid choice! Please try again.")
        return get_user_choice()

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def decide_winner(user, computer):
    print(f"\n🙋‍♀️ You chose: {user}")
    print(f"💻 Computer chose: {computer}")
    
    if user == computer:
        return "😐 It's a draw!"
    
    if (user == "rock" and computer == "scissors") or \
       (user == "paper" and computer == "rock") or \
       (user == "scissors" and computer == "paper"):
        return "🎉 You win!"
    else:
        return "💔 You lose!"

def play_game():
    print("\n🎮 Welcome to Rock-Paper-Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = decide_winner(user_choice, computer_choice)
        print(result)

        again = input("\n🔁 Play again? (yes/no): ").lower()
        if again != "yes":
            print("👋 Thanks for playing! See you next time.")
            break

# 🔄 Start the game
play_game()

