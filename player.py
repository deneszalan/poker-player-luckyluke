#!/usr/bin/env python

class Player:
    VERSION = "All-in 1"

    def anyCardRankEqual(self, cards, rank):
        for card in cards:
            if card["rank"]==rank:
                return True
        return False

    def isPair(self, cards):
        cards[0]["rank"]==cards[1]["rank"]

    def betRequest(self, game_state):
        # print "Hello"

        me = game_state["players"][game_state["in_action"]]
        mycards = me["hole_cards"]

        # print me
        # print mycards
        if self.isPair(mycards) or \
                (mycards[0]["suit"]==mycards[1]["suit"] and (self.anyCardRankEqual(mycards, 'A') or self.anyCardRankEqual(mycards, 'K'))):
            return int(me.stack)

        return 0

    def showdown(self, game_state):
        pass

