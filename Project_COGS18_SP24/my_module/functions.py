import random
import os
from my_module.classes import Game


                 
def display_grid(grid_size, player_pos, exit_pos, character):
    """
    Clears the screen and displays the current state of a grid with specified
    dimensions and locations. 

    Parameters
    ----------
    grid_size: int
        Determines the dimensions of the grid to be generated
    player_position: list containing ints
        A list of coordinates representing the player's position on the grid. 
    exit_pos: tuple containing ints
        A tuple of coordinates representing the exit's position on the grid.
    character: str
        A character to visually represent the player character on the grid.

    Returns
    -------
    None (This function does not return a value. It prints the generated grid in the console.)

    This function requires the "os" module to be imported.
    """

    os.system("clear")
    
    #Generates list which contains the values on the map
    grid_list = [['.'] * grid_size for columns in range(grid_size)]
    grid_list[player_pos[0]][player_pos[1]] = character
    grid_list[exit_pos[0]][exit_pos[1]] = "‡"
                        
    #Organizes grid_list into a visual to be printed in the console
    for row in grid_list:
        print(" ".join(row))
    


def update_pos(move, player_pos, grid_size):
    """
    Updates the player's position on the grid based on a movement command. 
    
    Parameters
    ----------
    move: str
        A character "w","a","s", or "d" representing a valid move.
    player_pos: list containing ints
        A list representing the player's current position on the grid. 
    grid_size: int
        Determines the dimensions of the current grid (rows x columns)
    
    Returns
    -------
    A list of integers representing the coordinates of the updated position 
    of the player. If the move is invalid (out of bounds) the original 
    position is returned. 
    """

    directions = {
        "w": (-1, 0),  # Up
        "s": (1, 0),   # Down
        "a": (0, -1),  # Left
        "d": (0, 1)    # Right
    }
    
    #assigns the player a new position based on their choice of move
    direction = directions[move]
    new_position = [player_pos[0] + direction[0], player_pos[1] + direction[1]]
    
    #Checks that the player's move is within the grid bounds. 
    if 0 <= new_position[0] < grid_size and 0 <= new_position[1] < grid_size:
        
        return new_position
               
    else:
               
        print("Invalid Move(Out of Bounds)")
        return player_pos
    
def trigger_event():

    """
    Triggers an event that places the player in a scenario and asks a question 
    that they need to answer. They will be prompted to keep trying until they 
    provide the correct answer. 

    Parameters
    ----------
    None

    Returns
    -------
    True (Boolean) when the player inputs the correct answer.

    Requires the "random" module to be imported.
    """
    scenarios = ["You are compelled to sit down at the nearest desk with a\n" + 
                 "pencil and paper in hand. On this paper, you are asked to \n" +
                 "solve the following problem:\n",
                 "The projector unexpectedly turns on, and you see the \n" +
                 "following problem displayed on the classroom screen:\n",
                 "You don’t know where it’s coming from, but you hear \n" +
                 "aguely familiar voice greet you, and it tells you to\n" +
                 "consider the problem:\n"]
    
    questions = {
            "Find the derivative of π²." : "0",
            "Use the Chain Rule to calculate f(r(t)) at t = 0. \nf(x,y) = 6sin(xy), r(t) = <e²ᵗ, e³ᵗ>" : "30cos(1)",
            "Find the speed over the path \nr(t) = <sin(3t),cos(6t), cos(7t)> at t = π/2" : "7",
            "Find the global minimum value of the function \nf(x,y) = x² + y² -4x -6y on x ≥ 0, 0 ≤ y ≤  5, y ≥ x" : "-13",
            "Calculate the volume of the parallelepiped spanned by \nu = <2,0,3>, v = <2,4,1>, w = <-4,3,6>" : "108"
        }
    
    #Chooses a random question-answer set to ask the player
    scene = random.choice(scenarios)
    prompt, answer = random.choice(list(questions.items())) 
    
    print(scene) 
    print(prompt)
    
    #Loop which prompts the user for the answer and returns True when they get it correct
    while True:

        player_ans = input("Your answer?: ")

        if player_ans.lower() == answer.lower():
            
            return True

        else:

            print("Wrong!! try again.")

def start_game():
    """
    Starts a game where the player has to navigate a grid, answer math 
    questions, and find an exit. This function initializes a new game, 
    allows the player to move on the grid using the W,A,S,D kays, and 
    triggers random questions. The game will continue until the player 
    reaches the exit.

    Parameters
    ----------
    None

    Returns
    -------
    None (This function continuously prompts the player for input and 
    updates the game state until the game ends.)

    This function requires the "random" module and my class "Game" to be imported.

    """
    game = Game()
    print("You open your eyes and find yourself dead center in an empty \n" +
          "classroom, unable to remember how you ended up here. Though the \n" +
          "room is dimly lit, you can't pinpoint where the light is coming from.\n" +
          "There are no windows, no LEDs on the ceiling, and not another soul in \n" + 
          "sight. You feel a sense of urgency to leave… that you have something\n" + 
          "important to do outside of here.\n\n")
    print("Luckily, almost as if you willed it to do so, you notice a door swing open \n" +
          "along one of the bare walls of the classroom.\n\n")
    print("Time to leave.\n\n")

    grid_size, player_pos, exit_pos, character = game.initial_input()
    
    #Defines what is considered a valid input for directions
    directions = {
            "w": (-1, 0),  # Up
            "s": (1, 0),   # Down
            "a": (0, -1),  # Left
            "d": (0, 1)    # Right
        }

    #Loop which continuously takes user input and only ends when the user reaches the exit. 
    while True:
        
        display_grid(grid_size, player_pos, exit_pos, character)
        player_move = input("Use W, A, S, D to move: ").lower()
        
        #Check if player_move is valid (WASD)
        while player_move not in directions:

            player_move = input("\n Please use W, A, S, D to move: ").lower()
        
        player_pos = update_pos(player_move, player_pos, grid_size)
        
        #When the post-move position equals the exit position the game ends
        if player_pos[0] == exit_pos[0] and player_pos[1] == exit_pos[1]:

            print("Congratulations! Despite being held back by cryptic\n" + 
                  "challenges, you made it to the exit!\n\n")
            print("After setting foot in the exit's doorway, the world \n" + 
                  "you just experienced disappears beneath you...\n\n")
            print("You jolt awake at your real-world desk, where your\n" + 
                  "laptop and notebook were left open from a long night \n" + 
                  "of studying. You tap your phone, which says that it’s\n" + 
                  "7:18 a.m. This peaceful Saturday morning, you have a\n" + 
                  "calculus final at 8.\n\n")
            print("Good luck! I hope studying in your dream helped :)")
            
            
            break

        #50% chance of triggering an event (question)
        if random.random() < 0.5: 


            correct = trigger_event()

            if correct:
                print("Correct!")
                
                

