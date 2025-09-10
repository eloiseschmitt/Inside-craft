POINT_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]
WIN_MIN = 4
WIN_LEAD = 2

class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name) -> None:
        if player_name == "player1":
            self.player1_points += 1
        else:
            self.player2_points += 1

    def score(self) -> str:
        if self.player1_points == self.player2_points:
            return self._tied_score()
        if self.player1_points >= WIN_MIN or self.player2_points >= WIN_MIN:
            return self._advantage_or_win()
        return self._normal_score()

    def _normal_score(self) -> str:
        left = POINT_NAMES[self.player1_points]
        right = POINT_NAMES[self.player2_points]
        return f"{left}-{right}"

    def _advantage_or_win(self) -> str:
        minus_result = self.player1_points - self.player2_points
        if minus_result == 1:
            return "Advantage player1"
        if minus_result == -1:
            return "Advantage player2"
        if minus_result >= WIN_LEAD:
            return "Win for player1"
        return "Win for player2"

    def _tied_score(self) -> str:
        return {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.player1_points, "Deuce")
