__author__ = 'salacz'

from player import Player
import unittest

class RankSuite(unittest.TestCase):
    def testBet(self):
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

    def testPairs(self):
        cards = [                            # Finally the array of community cards.
                                             {
                                                 "rank": "6",                    # Rank of the card. Possible values are numbers 2-10 and J,Q,K,A
                                                 "suit": "hearts"                # Suit of the card. Possible values are: clubs,spades,hearts,diamonds
                                             },
                                             {
                                                 "rank": "K",
                                                 "suit": "spades"
                                             },
                                             {
                                                 "rank": "A",
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
        p=Player()
        ranks, suits = p.getCardSorts(cards)
        self.assertTrue(p.hasPair(ranks))
        self.assertTrue(p.twoPairs(ranks))
        self.assertFalse(p.hasDrill(ranks))
        self.assertFalse(p.hasFull(ranks))
        self.assertFalse(p.hasPoker(ranks))

    def testDrill(self):
        cards = [                            # Finally the array of community cards.
                                             {
                                                 "rank": "6",                    # Rank of the card. Possible values are numbers 2-10 and J,Q,K,A
                                                 "suit": "hearts"                # Suit of the card. Possible values are: clubs,spades,hearts,diamonds
                                             },
                                             {
                                                 "rank": "A",
                                                 "suit": "spades"
                                             },
                                             {
                                                 "rank": "6",
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
        p=Player()
        ranks, suits = p.getCardSorts(cards)
        self.assertTrue(p.hasPair(ranks))
        self.assertFalse(p.twoPairs(ranks))
        self.assertTrue(p.hasDrill(ranks))
        self.assertTrue(p.hasFull(ranks))
        self.assertFalse(p.hasPoker(ranks))

    def testPoker(self):
        cards = [                            # Finally the array of community cards.
                                             {
                                                 "rank": "A",                    # Rank of the card. Possible values are numbers 2-10 and J,Q,K,A
                                                 "suit": "diamonds"              # Suit of the card. Possible values are: clubs,spades,hearts,diamonds
                                             },
                                             {
                                                 "rank": "A",
                                                 "suit": "spades"
                                             },
                                             {
                                                 "rank": "6",
                                                 "suit": "spades"
                                             },
                                             {
                                                 "rank": "A",
                                                 "suit": "hearts"
                                             },
                                             {
                                                 "rank": "A",
                                                 "suit": "clubs"
                                             }
        ]
        p=Player()
        ranks, suits = p.getCardSorts(cards)
        self.assertFalse(p.hasPair(ranks))
        self.assertFalse(p.twoPairs(ranks))
        self.assertFalse(p.hasDrill(ranks))
        self.assertFalse(p.hasFull(ranks))
        self.assertTrue(p.hasPoker(ranks))

    def testStraight(self):
        cards1 = [                            # Finally the array of community cards.
                                             {
                                                 "rank": "5",                    # Rank of the card. Possible values are numbers 2-10 and J,Q,K,A
                                                 "suit": "diamonds"              # Suit of the card. Possible values are: clubs,spades,hearts,diamonds
                                             },
                                             {
                                                 "rank": "6",
                                                 "suit": "spades"
                                             },
                                             {
                                                 "rank": "7",
                                                 "suit": "spades"
                                             },
                                             {
                                                 "rank": "8",
                                                 "suit": "hearts"
                                             },
                                             {
                                                 "rank": "J",
                                                 "suit": "clubs"
                                             }
        ]
        cards2 = [                            # Finally the array of community cards.
                                             {
                                                 "rank": "8",                    # Rank of the card. Possible values are numbers 2-10 and J,Q,K,A
                                                 "suit": "diamonds"              # Suit of the card. Possible values are: clubs,spades,hearts,diamonds
                                             },
                                             {
                                                 "rank": "9",
                                                 "suit": "spades"
                                             },
                                             {
                                                 "rank": "10",
                                                 "suit": "spades"
                                             },
                                             {
                                                 "rank": "J",
                                                 "suit": "hearts"
                                             },
                                             {
                                                 "rank": "Q",
                                                 "suit": "clubs"
                                             }
        ]
        p=Player()
        self.assertFalse(p.hasStraight(cards1))
        self.assertTrue(p.hasStraight(cards2))

if __name__ == '__main__':
    unittest.main()
