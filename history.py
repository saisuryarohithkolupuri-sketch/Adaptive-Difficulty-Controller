# history.py

class ScoreHistory:
    def __init__(self):
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_recent_scores(self, window_size):
        return self.scores[-window_size:]