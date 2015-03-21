#!/usr/bin/env python
from ranking import Ranking

STRAIGHT_CARDS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

class Player():
    VERSION = "All-in 1"

    def anyCardRankEqual(self, cards, rank):
        for card in cards:
            if card["rank"]==rank:
                return True
        return False

    def isPair(self, cards):
        cards[0]["rank"]==cards[1]["rank"]

    def getCardSorts(self, allcards):
        ranks={}
        suits={}
        for card in allcards:
            if not ranks.has_key(card["rank"]):
                ranks[card["rank"]]=1
            else:
                ranks[card["rank"]]+=1
            if card["suit"] not in suits:
                suits[card["suit"]]=1
            else:
                suits[card["suit"]]+=1

        print allcards
        print ranks
        print suits
        return (ranks, suits)

    def hasPair(self, ranks):
        return 2 in ranks.values()

    def twoPairs(self, ranks):
        counts=ranks.values()
        return 2 == counts.count(2)

    def hasDrill(self, ranks):
        return 3 in ranks.values()

    def hasPoker(self, ranks):
        return 4 in ranks.values()

    def hasFull(self, ranks):
        return (2 in ranks.values()) and (3 in ranks.values())

    def hasFlush(self, suits):
        return 5 in suits.values() or 6 in suits.values() or 7 in suits.values()

    def hasStraight(self, cards):
        for j in range(len(cards)-4):
            i = STRAIGHT_CARDS.index(cards[j]["rank"])
            straight = STRAIGHT_CARDS[i:i+5]
            if cards[j:j+5] == straight:
                return True
        return False

    def getRank(self, allcards, ranks, suits):
        if len(allcards)!=5:
            return 0

        return 0

    def betRequest(self, game_state):
        bet = 0
        myself = game_state["players"][game_state["in_action"]]
        my_cards = myself["hole_cards"]

        ranking = Ranking(my_cards)
        chen_ranking = ranking.get_chen_ranking()

        is_preflop = len(game_state["community_cards"]) == 0

        if is_preflop:
            if chen_ranking >= 5.5:
                bet = myself["stack"]
        else:
            bet = max(100, int(game_state["minimum_raise"]))

        return int(bet)


    def showdown(self, game_state):
        pass

if __name__ == "__main__":
    pass