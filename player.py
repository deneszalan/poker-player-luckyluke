#!/usr/bin/env python
from ranking import Ranking

STRAIGHT_VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def cmpValue(a, b):
    return STRAIGHT_VALUES.index(a["rank"])-STRAIGHT_VALUES.index(b["rank"])

def getValues(cards):
    result = []
    for card in cards:
        result += [card["rank"]]
    return result

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

        # print allcards
        # print ranks
        # print suits
        return (ranks, suits)

    def hasPair(self, ranks):
        return 2 in ranks.values()

    def hasTwoPairs(self, ranks):
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
        cards = sorted(cards, cmp=cmpValue)
        values = getValues(cards)
        # print cards
        for j in range(len(cards)-4):
            i = STRAIGHT_VALUES.index(values[j])
            straight = STRAIGHT_VALUES[i:i+5]
            if values[j:j+5] == straight:
                return True
        return False

    def hasStraightFlush(self, cards):
        for j in range(len(cards)-4):
            cards2check = cards[j:j+5]
            if self.hasFlush(cards2check) and self.hasStraight(cards2check):
                return True
        return False

    # def sort(self, cards):
    #     for i in range(len(cards)-1):
    #         for j in range(i+1, len(cards)):
    #             if (cards[i]["rank"]>cards[j]["rank"]):
    #                 card = cards[i]
    #                 cards[i] = cards[j]
    #                 cards[j] = card

    def getRank(self, allcards, ranks, suits):
        if len(allcards)!=5:
            return 0
        if self.hasStraightFlush(allcards):
            return 8
        if self.hasPoker(allcards):
            return 7
        if self.hasFull(allcards):
            return 6
        if self.hasFlush(allcards):
            return 5
        if self.hasStraight(allcards):
            return 4
        if self.hasDrill(allcards):
            return 3
        if self.hasTwoPairs(allcards):
            return 2
        if self.hasPair(allcards):
            return 1
        return 0

    def betRequest(self, game_state):
        bet = 0

        try:
            myself = game_state["players"][game_state["in_action"]]
            my_cards = myself["hole_cards"]

            ranking = Ranking(my_cards)
            chen_ranking = ranking.get_chen_ranking()

            is_preflop = len(game_state["community_cards"]) == 0
            active_player_count = len(filter(lambda player: player["status"] == "active", game_state["players"]))

            all_in_value = myself["stack"]

            if is_preflop:
                if active_player_count == 2:
                    if chen_ranking >= 4.5:
                        bet = all_in_value
                elif active_player_count == 3:
                    if chen_ranking >= 5.5:
                        bet = all_in_value
                elif active_player_count == 4:
                    if chen_ranking >= 6:
                        bet = all_in_value

                minimum_raise = int(game_state["minimum_raise"])
                small_blind = int(game_state["small_blind"])

                did_somebody_raise = minimum_raise >= small_blind * 3

                if minimum_raise > small_blind*8:
                    if chen_ranking >= 7.5:
                        bet = all_in_value

                if not did_somebody_raise:
                    bet = minimum_raise * 2 + 1

            else:
                #out_player_count =
                bet = max(100, int(game_state["minimum_raise"]))
        except:
            print "Meghaltam :("

        return int(bet)


    def showdown(self, game_state):
        pass

if __name__ == "__main__":
    pass