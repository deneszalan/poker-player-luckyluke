__author__ = 'salacz'

from player import Player

def test1():
    p=Player()
    gameState = {
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
        "community_cards": [                            # Finally the array of community cards.
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

    p.betRequest(gameState)

if __name__ == '__main__':
    test1()