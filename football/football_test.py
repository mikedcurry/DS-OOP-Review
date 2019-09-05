import unittest
from players import Player, Quarterback
from possible_values import *
from game import Game
from season import *
# TODO - some things you can add...

# done: import the `season` file and make sure generate_random_games only

# makes games with appropriate team names (and never has a team playing itself)

# Complete the FootballGameTest


class FootballGameTest(unittest.TestCase):
    '''test the class'''
    def test_field_goal_made(self):
       game1 = Game(teams=['h', 'j'])
       score1 = game1.score['h']
       game1.field_goal('h')
       self.assertEqual(game1.score['h'], (score1+3))

    def test_get_winner(self):
        game2 = Game(teams=['h', 'j'], 
                     score={'h':1, 'j':0})
        game2.get_winning_team()
        self.assertEqual(game2.winning_team_, 'h')

    


class FootballPlayerTest(unittest.TestCase):
    '''Check the default values for Player and Quarterback
    yards=120, touchdowns=5, safety=1,
                 interceptions=0
    '''
    def test_default_player_yards(self):
        player = Player(name='Dude')
        self.assertEqual(player.yards, 125)

    def test_player_yards_set_to(self):
        player = Player(name='OtherDude', yards=150)
        self.assertEqual(player.yards, 150)

    def test_default_qb_interceptions(self):
        qb = Quarterback(name='FancyDude')
        self.assertEqual(qb.interceptions, 4)

    def test_default_qb_completed_passes(self):
        qb = Quarterback()
        self.assertEqual(qb.completed_passes, 20)

    def test_passing_score(self):
        qb = Quarterback()
        self.assertEqual((20 - (2 * 4)), qb.passing_score())

    


if __name__ == '__main__':
    unittest.main()
