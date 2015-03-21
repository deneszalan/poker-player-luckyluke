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

    def get_chen_rank(self):
        chen = 0
        ranks = [card["rank"] for card in self._cards]

        values = [self._rank2value[rank] for rank in ranks]
        chen_values = [self._rank2chenvalue[rank] for rank in ranks]

        chen += max(chen_values)


        #values = [self._rank2chenvalue[card["rank"]] for card in self._cards]
        #print values




        return chen

if __name__ == "__main__":
    cards = [{
                        "rank": "6",                    # Rank of the card. Possible values are numbers 2-10 and J,Q,K,A
                        "suit": "hearts"                # Suit of the card. Possible values are: clubs,spades,hearts,diamonds
                    },
                    {
                        "rank": "K",
                        "suit": "spades"
                    }
                  ]
    r = Ranking(cards)


    rank = r.get_chen_rank()
    print rank