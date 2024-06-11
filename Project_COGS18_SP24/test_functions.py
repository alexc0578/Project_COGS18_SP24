"""
Testing my functions and methods
"""

from my_module.functions import update_pos, trigger_event
from my_module.classes import Game

import unittest
from unittest.mock import patch

def test_update_pos():
    player_pos = [0,3]
    assert callable(update_pos)
    assert update_pos("s", player_pos, 5) == [1,3]
    assert update_pos("w", player_pos, 5) == player_pos

"""
References
----------
I used the following sources to help me figure out how to test functions that 
take user input and involve randomly generated variables. I learned how to use
"patch" to simulate user input and a random choice and organize my tests into 
classes comprised of methods that would run multiple tests on various cases. I
used these concepts to make my own tests below.

Open AI: ChapGPT
Stack Overflow: https://stackoverflow.com/questions/55209306/patch-my-function-to-random-randint-function?rq=3
Andressa.dev: https://andressa.dev/2019-07-20-using-pach-to-test-inputs/
"""


class TestTriggerEvent(unittest.TestCase):

    @patch('builtins.input', side_effect=['108'])
    @patch('builtins.print')
    @patch('random.choice', side_effect=[
        "You are compelled to sit down at the nearest desk with a pencil and paper \n"
        "in hand. On this paper, you are asked to solve the following problem:",
        ("Calculate the volume of the parallelepiped spanned by \nu = <2,0,3>, "
         "v = <2,4,1>, w = <-4,3,6>", "108")
    ])

    #Test that simulates the user inputting the correct answer on the first attempt
    def test_correct_answer_first_try(self, mock_random_choice, mock_print, mock_input):
        result = trigger_event()
        self.assertTrue(result)
        mock_print.assert_any_call("You are compelled to sit down at the nearest desk with a pencil and paper \nin hand. On this paper, you are asked to solve the following problem:")
        mock_print.assert_any_call("Calculate the volume of the parallelepiped spanned by \nu = <2,0,3>, v = <2,4,1>, w = <-4,3,6>")

    @patch('builtins.input', side_effect=['5', '50', '108'])
    @patch('builtins.print')
    @patch('random.choice', side_effect=[
        "The projector unexpectedly turns on, and you see the following problem\n"
        "displayed on the screen:",
        ("Calculate the volume of the parallelepiped spanned by \nu = <2,0,3>, "
         "v = <2,4,1>, w = <-4,3,6>", "108")
    ])

    #Test that checks the function will continue to prompt the user for input after incorrect attempts
    def test_correct_answer_after_attempts(self, mock_random_choice, mock_print, mock_input):
        result = trigger_event()
        self.assertTrue(result)
        mock_print.assert_any_call("The projector unexpectedly turns on, and you see the following problem\ndisplayed on the screen:")
        mock_print.assert_any_call("Calculate the volume of the parallelepiped spanned by \nu = <2,0,3>, v = <2,4,1>, w = <-4,3,6>")
        mock_print.assert_any_call("Wrong!! try again.")
        self.assertEqual(mock_input.call_count, 3)

class TestGame(unittest.TestCase):

    @patch('builtins.input', side_effect=['a', 'a'])
    @patch('random.choice', side_effect=[(0, 0), (0, 1)])
    
    #Simulates the user inputting "a" for their character choice and "a" for easy mode
    def test_initial_input_easy(self, mock_random_choice, mock_input):
        game = Game()
        result = game.initial_input()
        self.assertEqual(result, (5, [2, 2], (0, 0), '¤'))

    @patch('builtins.input', side_effect=['b', 'b'])
    @patch('random.choice', side_effect=[(0, 0), (0, 1)])
    
    #Simulates the user inputting "b" for their character choice and "b" for medium mode
    def test_initial_input_medium(self, mock_random_choice, mock_input):
        game = Game()
        result = game.initial_input()
        self.assertEqual(result, (15, [7, 7], (0, 0), '§'))

    @patch('builtins.input', side_effect=['c', 'c'])
    @patch('random.choice', side_effect=[(0, 0), (0, 1)])
    
    #Simulates the user inputting "c" for their character choice and "c" for hard mode
    def test_initial_input_hard(self, mock_random_choice, mock_input):
        game = Game()
        result = game.initial_input()
        self.assertEqual(result, (25, [12, 12], (0, 0), '×'))