#!/usr/bin/env python

STRAIGHT_VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def cmpValue(a, b):
    return STRAIGHT_VALUES.index(a["rank"])-STRAIGHT_VALUES.index(b["rank"])

def getValues(cards):
    result = []
    for card in cards:
        result += [card["rank"]]
    return result

class Ranking():
    def __init__(self, cards):
        self._rank2value = {"J": 11, "Q": 12, "K": 13, "A": 14}
        self._rank2chenvalue = {"J": 6, "Q": 7, "K": 8, "A": 10}
        self._cards = cards
        for i in xrange(2,11):
            self._rank2chenvalue[str(i)] = i/2.0
            self._rank2value[str(i)] = i
        self._ranks, self._suits = Ranking._computeRanksAndSuits(self._cards)

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

    @classmethod
    def _computeRanksAndSuits(cls, cards):
        ranks = dict()
        suits = dict()
        for card in cards:
            rank = card["rank"]
            suit = card["suit"]
            ranks[rank] = ranks.get(rank, 0) + 1
            suits[suit] = suits.get(suit, 0) + 1
        return ranks, suits

    def hasPair(self):
        return 2 in self._ranks.values()

    def hasTwoPairs(self):
        return 2 == self._ranks.values().count(2)

    def hasDrill(self):
        return 3 in self._ranks.values()

    def hasPoker(self):
        return 4 in self._ranks.values()

    def hasFull(self):
        return (2 in self._ranks.values()) and (3 in self._ranks.values())

    def hasFlush(self):
        return 5 in self._suits.values() or 6 in self._suits.values() or 7 in self._suits.values()

    def hasStraight(self):
        cards = sorted(self._cards, cmp=cmpValue)
        values = getValues(cards)
        # print cards
        for j in range(len(cards)-4):
            i = STRAIGHT_VALUES.index(values[j])
            straight = STRAIGHT_VALUES[i:i+5]
            if values[j:j+5] == straight:
                return True
        return False

    def hasStraightFlush(self):
        result = False
        for j in range(len(self._cards)-4):
            r5=Ranking(self._cards[j:j+5])
            if r5.hasFlush() and r5.hasStraight():
                result = True
                break
        return result

    def getRanking(self):
        # if len(self._cards)<5:
        #     return 0
        if self.hasStraightFlush():
            return 8
        if self.hasPoker():
            return 7
        if self.hasFull():
            return 6
        if self.hasFlush():
            return 5
        if self.hasStraight():
            return 4
        if self.hasDrill():
            return 3
        if self.hasTwoPairs():
            return 2
        if self.hasPair():
            return 1
        return 0

    def highest_card_value(self):
        values = [self._rank2value[c["rank"]] for c in self._cards]
        pass

if __name__ == "__main__":
    cards = [       {
                        "rank": "2",                    # Rank of the card. Possible values are numbers 2-10 and J,Q,K,A
                        "suit": "hearts"                # Suit of the card. Possible values are: clubs,spades,hearts,diamonds
                    },
                    {
                        "rank": "4",                    # Rank of the card. Possible values are numbers 2-10 and J,Q,K,A
                        "suit": "hearts"                # Suit of the card. Possible values are: clubs,spades,hearts,diamonds
                    },
                    {
                        "rank": "6",                    # Rank of the card. Possible values are numbers 2-10 and J,Q,K,A
                        "suit": "hearts"                # Suit of the card. Possible values are: clubs,spades,hearts,diamonds
                    },
                    {
                        "rank": "8",                    # Rank of the card. Possible values are numbers 2-10 and J,Q,K,A
                        "suit": "hearts"                # Suit of the card. Possible values are: clubs,spades,hearts,diamonds
                    },
                    {
                        "rank": "K",
                        "suit": "spades"
                    }
                  ]
    r = Ranking(cards)


    rank = r.getRanking()
    #print rank
    print r.highest_card_value()
