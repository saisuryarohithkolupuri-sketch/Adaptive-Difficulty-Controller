# controller.py

from config import EASY_MAX, MEDIUM_MAX, WINDOW_SIZE, COOLDOWN
from evaluator import calculate_average


class AdaptiveDifficultyController:

    def __init__(self):
        self.current_difficulty = "Medium"
        self.cooldown_counter = 0

    def determine_difficulty(self, average_score):

        if average_score <= EASY_MAX:
            return "Easy"

        elif average_score <= MEDIUM_MAX:
            return "Medium"

        else:
            return "Hard"

    def update_difficulty(self, score_history):

        recent_scores = score_history.get_recent_scores(WINDOW_SIZE)

        average_score = calculate_average(recent_scores)

        suggested_difficulty = self.determine_difficulty(average_score)

        # Prevent oscillation using cooldown
        if self.cooldown_counter > 0:
            self.cooldown_counter -= 1
            return self.current_difficulty, average_score

        # Change difficulty only if needed
        if suggested_difficulty != self.current_difficulty:
            self.current_difficulty = suggested_difficulty
            self.cooldown_counter = COOLDOWN

        return self.current_difficulty, average_score