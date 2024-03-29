"""DAY7_Part1"""
from pathlib import Path
from pprint import pprint


class CamelCardsHand:
    """Class to represent a hand of cards"""

    cards: str
    bet: int
    score: int

    def __init__(self, cards: str, bet: int) -> None:
        """Initialize the hand of cards"""
        self.cards = cards
        self.bet = int(bet)
        self.score = self.get_score()

    def rank_cards(self) -> int:
        """Return the score of the cards"""
        ranking = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        return int("".join([f"{ranking.index(card):02}" for card in self.cards]))

    def rank_hand(self) -> int:
        """Return the rank of the hand of cards"""
        hank_rankings = {
            (5,): 7000000000000,
            (1, 4): 6000000000000,
            (2, 3): 5000000000000,
            (1, 1, 3): 4000000000000,
            (1, 2, 2): 3000000000000,
            (1, 1, 1, 2): 2000000000000,
            (1, 1, 1, 1, 1): 1000000000000,
        }

        current_hand = [self.cards.count(x) for x in set(self.cards)]
        current_hand.sort()
        return hank_rankings[tuple(current_hand)]

    def get_score(self) -> int:
        """Return the score of the hand of cards"""
        hand_ranking = self.rank_hand()
        cards_score = self.rank_cards()
        return hand_ranking + cards_score

    def __repr__(self) -> str:
        """Return the representation of the hand of cards"""
        return f"{self.cards} {self.bet}"

    def __lt__(self, other: "CamelCardsHand") -> bool:
        """Return true if the score of the hand is lower than the other"""
        return self.score < other.score

    def __gt__(self, other: "CamelCardsHand") -> bool:
        """Return true if the score of the hand is greater than the other"""
        return self.score > other.score


def main() -> None:
    """Main"""
    input_file = Path("./Advent_of_code/2023/DAY7_Part1.txt")
    input_data = input_file.read_text().splitlines()

    camel_cards_hands = [CamelCardsHand(*line.split(" ")) for line in input_data]

    camel_cards_hands.sort()

    winnings = [hand.bet * ranking for ranking, hand in enumerate(camel_cards_hands, start=1)]

    pprint(sum(winnings))


main()
