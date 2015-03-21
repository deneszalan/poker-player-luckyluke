#!/usr/bin/env python
from ranking import Ranking


class Player():
    VERSION = "All-in 1"

    def betRequest(self, game_state):
        bet = 0
        all_my_money = 0

        try:
            myself = game_state["players"][game_state["in_action"]]
            cards_hand = myself["hole_cards"]
            cards_desk = game_state["community_cards"]
            cards_all = cards_hand + cards_desk
            all_my_money = int(myself["stack"])

            ranking_service_all_cards = Ranking(cards_all)
            ranking_service_hand = Ranking(cards_hand)

            #ranking = Ranking(cards_hand)
            chen_ranking = ranking_service_all_cards.get_chen_ranking()
            ranking = ranking_service_all_cards.getRanking()

            is_preflop = len(game_state["community_cards"]) == 0
            active_player_count = len(filter(lambda player: player["status"] == "active", game_state["players"]))

            all_in_value = myself["stack"]
            minimum_raise = int(game_state["minimum_raise"])
            small_blind = int(game_state["small_blind"])



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

                did_somebody_raise = minimum_raise >= small_blind * 3

                if minimum_raise > small_blind*8:
                    if chen_ranking >= 7.5:
                        bet = all_in_value

                if not did_somebody_raise:
                    bet = minimum_raise * 2

            else:
                TWO_PAIRS = 2
                if ranking == 0:
                    bet = 0
                elif ranking == 1:
                    bet = 2 * small_blind
                    # desk_card_values = [c for c in cards_desk]
                    # largest_desk_card_value = m
                elif ranking >= TWO_PAIRS:
                    bet = all_in_value
                #out_player_count =
                #bet = max(100, int(game_state["minimum_raise"]))
        except:
            print "Meghaltam :("

        return int(min(bet, all_my_money))


    def showdown(self, game_state):
        pass

if __name__ == "__main__":
    p = Player()
    game_state = {
            "small_blind": 10,
            "current_buy_in": 320,
            "pot": 400,
            "minimum_raise": 240,
            "dealer": 1,
            "orbits": 7,
            "in_action": 1,
            "players": [
                {
                    "id": 0,
                    "name": "Albert",
                    "status": "active",
                    "version": "Default random player",
                    "stack": 1010,                          # Amount of chips still available for the player. (Not including
                    "bet": 320                              # The amount of chips the player put into the pot
                },
                {
                    "id": 1,                                # Your own player looks similar, with one extension.
                    "name": "Bob",
                    "status": "active",
                    "version": "Default random player",
                    "stack": 1590,
                    "bet": 80,
                    "hole_cards": [                         # The cards of the player. This is only visible for your own player
                        {
                            "rank": "6",                    # Rank of the card. Possible values are numbers 2-10 and J,Q,K,A
                            "suit": "hearts"                # Suit of the card. Possible values are: clubs,spades,hearts,diamonds
                        },
                        {
                            "rank": "K",
                            "suit": "spades"
                        }
                    ]
                },
                {
                    "id": 2,
                    "name": "Chuck",
                    "status": "out",
                    "version": "Default random player",
                    "stack": 0,
                    "bet": 0
                }
            ],
            "community_cards": [
                {
                    "rank": "4",
                    "suit": "spades"
                },
                {
                    "rank": "A",
                    "suit": "hearts"
                },
                {
                    "rank": "6",
                    "suit": "clubs"
                }
            ]
        }
    print p.betRequest(game_state)