__author__ = 'salacz'

from player import Player
from ranking import Ranking
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

        p.betRequest(gameState)

    def testPairs(self):
        cards = [
                                             {
                                                 "rank": "6",
                                                 "suit": "hearts"
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
        r=Ranking(cards)
        self.assertTrue(r.hasPair())
        self.assertTrue(r.hasTwoPairs())
        self.assertFalse(r.hasDrill())
        self.assertFalse(r.hasFull())
        self.assertFalse(r.hasPoker())

    def testDrill(self):
        cards = [
                                             {
                                                 "rank": "6",
                                                 "suit": "hearts"
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
        r=Ranking(cards)
        self.assertTrue(r.hasPair())
        self.assertFalse(r.hasTwoPairs())
        self.assertTrue(r.hasDrill())
        self.assertTrue(r.hasFull())
        self.assertFalse(r.hasPoker())

    def testPoker(self):
        cards = [
                                             {
                                                 "rank": "A",
                                                 "suit": "diamonds"
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
        r=Ranking(cards)
        self.assertFalse(r.hasPair())
        self.assertFalse(r.hasTwoPairs())
        self.assertFalse(r.hasDrill())
        self.assertFalse(r.hasFull())
        self.assertTrue(r.hasPoker())

    def testFlush(self):
        cards1 = [
                                             {
                                                 "rank": "5",
                                                 "suit": "diamonds"
                                             },
                                             {
                                                 "rank": "2",
                                                 "suit": "diamonds"
                                             },
                                             {
                                                 "rank": "7",
                                                 "suit": "diamonds"
                                             },
                                             {
                                                 "rank": "8",
                                                 "suit": "clubs"
                                             },
                                             {
                                                 "rank": "8",
                                                 "suit": "diamonds"
                                             },
                                             {
                                                 "rank": "J",
                                                 "suit": "diamonds"
                                             }
        ]
        r=Ranking(cards1)
        self.assertTrue(r.hasFlush())

    def testStraight(self):
        cards1 = [
                                             {
                                                 "rank": "5",
                                                 "suit": "diamonds"
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
        r=Ranking(cards1)
        self.assertFalse(r.hasStraight())
        cards2 = [
                                             {
                                                 "rank": "8",
                                                 "suit": "diamonds"
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
        r=Ranking(cards2)
        self.assertTrue(r.hasStraight())
        cards3 = [
                                             {
                                                 "rank": "6",
                                                 "suit": "spades"
                                             },
                                             {
                                                 "rank": "7",
                                                 "suit": "hearts"
                                             },
                                             {
                                                 "rank": "2",
                                                 "suit": "diamonds"
                                             },
                                             {
                                                 "rank": "5",
                                                 "suit": "spades"
                                             },
                                             {
                                                 "rank": "8",
                                                 "suit": "clubs"
                                             },
                                             {
                                                 "rank": "9",
                                                 "suit": "clubs"
                                             }
        ]
        r=Ranking(cards3)
        self.assertTrue(r.hasStraight())
        cards4 = [
                                             {
                                                 "rank": "K",
                                                 "suit": "clubs"
                                             },
                                             {
                                                 "rank": "10",
                                                 "suit": "spades"
                                             },
                                             {
                                                 "rank": "Q",
                                                 "suit": "hearts"
                                             },
                                             {
                                                 "rank": "J",
                                                 "suit": "spades"
                                             },
                                             {
                                                 "rank": "9",
                                                 "suit": "diamonds"
                                             },
                                             {
                                                 "rank": "7",
                                                 "suit": "clubs"
                                             }
        ]
        r=Ranking(cards4)
        self.assertTrue(r.hasStraight())

    def testRanking(self):
        # r=Player()
        # r.get
        cards = [
                                             {
                                                 "rank": "6",
                                                 "suit": "hearts"
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
                                                 "rank": "Q",
                                                 "suit": "hearts"
                                             },
                                             {
                                                 "rank": "6",
                                                 "suit": "clubs"
                                             }
        ]
        r=Ranking(cards)
        self.assertEqual(1, r.getRanking())

        cards = [
                                             {
                                                 "rank": "6",
                                                 "suit": "hearts"
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
        r=Ranking(cards)
        self.assertEqual(2, r.getRanking())

        cards = [
                                             {
                                                 "rank": "6",
                                                 "suit": "hearts"
                                             },
                                             {
                                                 "rank": "K",
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
        r=Ranking(cards)
        self.assertEqual(3, r.getRanking())

        cards = [
                                             {
                                                 "rank": "10",
                                                 "suit": "spades"
                                             },
                                             {
                                                 "rank": "8",
                                                 "suit": "diamonds"
                                             },
                                             {
                                                 "rank": "J",
                                                 "suit": "hearts"
                                             },
                                             {
                                                 "rank": "9",
                                                 "suit": "spades"
                                             },
                                             {
                                                 "rank": "Q",
                                                 "suit": "clubs"
                                             }
        ]
        r=Ranking(cards)
        self.assertEqual(4, r.getRanking())

        cards = [
                                             {
                                                 "rank": "5",
                                                 "suit": "diamonds"
                                             },
                                             {
                                                 "rank": "2",
                                                 "suit": "diamonds"
                                             },
                                             {
                                                 "rank": "7",
                                                 "suit": "diamonds"
                                             },
                                             {
                                                 "rank": "8",
                                                 "suit": "clubs"
                                             },
                                             {
                                                 "rank": "8",
                                                 "suit": "diamonds"
                                             },
                                             {
                                                 "rank": "J",
                                                 "suit": "diamonds"
                                             }
        ]
        r=Ranking(cards)
        self.assertEqual(5, r.getRanking())

        cards = [
                                             {
                                                 "rank": "6",
                                                 "suit": "hearts"
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
        r=Ranking(cards)
        self.assertEqual(6, r.getRanking())

        cards = [
                                             {
                                                 "rank": "A",
                                                 "suit": "diamonds"
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
        r=Ranking(cards)
        self.assertEqual(7, r.getRanking())

        cards = [
                                             {
                                                 "rank": "8",
                                                 "suit": "spades"
                                             },
                                             {
                                                 "rank": "J",
                                                 "suit": "spades"
                                             },
                                             {
                                                 "rank": "Q",
                                                 "suit": "spades"
                                             },
                                             {
                                                 "rank": "10",
                                                 "suit": "spades"
                                             },
                                             {
                                                 "rank": "9",
                                                 "suit": "spades"
                                             }
        ]
        r=Ranking(cards)
        self.assertEqual(8, r.getRanking())

if __name__ == '__main__':
    unittest.main()
