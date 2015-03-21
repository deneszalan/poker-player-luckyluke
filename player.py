#!/usr/bin/env python
from ranking import Ranking


class Player():
    VERSION = "All-in 1"

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