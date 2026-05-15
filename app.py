# app.py

from history import ScoreHistory
from controller import AdaptiveDifficultyController

# Initialize system
history = ScoreHistory()
controller = AdaptiveDifficultyController()

print("=== Adaptive Difficulty Controller ===")

while True:

    user_input = input("\nEnter score (0-100) or 'q' to quit: ")

    if user_input.lower() == 'q':
        print("Exiting...")
        break

    try:
        score = int(user_input)

        if score < 0 or score > 100:
            print("Please enter a valid score between 0 and 100.")
            continue

        # Store score
        history.add_score(score)

        # Update difficulty
        difficulty, average = controller.update_difficulty(history)

        print(f"\nRecent Average Score: {average:.2f}")
        print(f"Current Difficulty: {difficulty}")

    except ValueError:
        print("Invalid input. Enter a number.")