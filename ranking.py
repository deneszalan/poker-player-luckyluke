#!/usr/bin/env python


class Ranking():
    def __init__(self, cards):
        self._rank2value = {"J": 11, "Q": 12, "K": 13, "A": 14}
        self._rank2chenvalue = {"J": 6, "Q": 7, "K": 8, "A": 10}
        self._cards = cards
        for i in xrange(2,11):
            self._rank2chenvalue[str(i)] = i/2.0
            self._rank2value[str(i)] = i
        print self._rank2chenvalue

    def get_chen_ranking(self):

        ranks = [card["rank"] for card in self._cards]
        suits = [card["suit"] for card in self._cards]
        values = [self._rank2value[rank] for rank in ranks]
        chen_values = [self._rank2chenvalue[rank] for rank in ranks]

        chen = max(chen_values)

        is_pair = ranks[0] == ranks[1]
        if is_pair:
            value = values[0]
            if value < 5:
                chen = 5
            elif value == 5:
                chen = 6
            else:
                chen *= 2

        same_suits = suits[0] == suits[1]
        if same_suits:
            chen += 2

        higher_value = max(values)
        lower_value = min(values)
        gap = higher_value - lower_value

        gap2minus = {
                2: -1,
                3: -2,
                4: -4
        }

        if gap in gap2minus:
            chen += gap2minus[gap]
        elif gap >= 5:
            chen -= 5

        if gap in [1, 2] and higher_value < 12:
            chen += 1

        return chen

if __name__ == "__main__":
    cards = [{
                        "rank": "7",                    # Rank of the card. Possible values are numbers 2-10 and J,Q,K,A
                        "suit": "hearts"                # Suit of the card. Possible values are: clubs,spades,hearts,diamonds
                    },
                    {
                        "rank": "6",
                        "suit": "spades"
                    }
                  ]
    r = Ranking(cards)


    rank = r.get_chen_ranking()
    print rank