import random

class Game():
    """
    A class for a simple game in which the player can choose a character,
    select a difficulty level, and navigate the grid to find the exit. 

    Attributes
    ----------
    character: str
        The character icon chosen by the user to visually represent the player
        position on the grid. 
    grid_size: int
        Determines the dimensions of the grid to be generated 
        (# of rows and columns).
    player_pos: list of ints
        The player's position on the grid as coordinates. 
    exit_pos: list of ints
        The exit's position on the grid as coordinates. 

    Methods
    -------
    __init__():
        Initializes a game with default attributes. 
    initial_input():
        Prompts the user to customize their character, select a difficulty level, 
        and generates positions for the player and exit on the grid. 
    
    References
    ----------
    Open AI: ChapGPT
        Helped me learn how to generate a set of coordinates in order to define
        the edges of a grid. 
    """
    
    def __init__(self):
        """
        Initializes the game by setting default values for character, grid_size, 
        player_pos, and exit_pos.
        """
        self.character = ""
        self.grid_size = 0
        self.player_pos = []
        self.exit_pos = []
    
    def initial_input(self):
        """
        Prompts the user to customize their character icon, select a difficulty level, and 
        generates a random exit along the borders of the grid and places the player in the 
        center of the grid. 
        
        Returns
        -------
        A tuple containing the grid_size, player's initial position, exit position, and the selected
        character icon.
        """
        #Loop in which player chooses their character from a predefined set.
        while True:

            char_choice = input("Choose a character icon: \n" +
                            "A)  ¤ \n" +
                            "B)  § \n" +
                            "C)  × \n" +
                            "D)  ø \n" +
                            "Type the character's corresponding letter to make your choice. \n").lower()


            if char_choice in ["a","b","c","d"]:

                if char_choice == "a":

                    self.character = "¤"
                    break

                elif char_choice == "b":

                    self.character = "§"
                    break       

                elif char_choice == "c":

                    self.character = "×"
                    break

                elif char_choice == "d":

                    self.character = "ø"
                    break
            
            #Keeps going until the player provides a valid input
            else:
                print("Please type a single letter A,B,C, or D \n")

        #Starts a loop in which promts the player to choose a difficulty level
        while True:

            diff_choice = input("Choose a difficulty level: \n" +
                            "A)  Easy \n" +
                            "B)  Medium \n" +
                            "C)  Hard \n" +
                            "Type the character's corresponding letter to make your choice. \n").lower()

            
            #Making sure the user input is within the characters "a","b", or "c" 
            if diff_choice in ["a","b","c"]:
            
            #Each choice of difficulty sets grid_size to a different value.
                if diff_choice == "a":

                    self.grid_size = 5

                    break

                elif diff_choice == "b":

                    self.grid_size = 15
                    break       

                elif diff_choice == "c":

                    self.grid_size = 25
                    break
            
            #Keeps going until the player provides a valid input
            else:
                print("Please type a single letter A,B,C, or D \n")
                
            
        #Player will start in the center of the grid.
        self.player_pos = [self.grid_size // 2, self.grid_size // 2]
                
        #The exit position is randomly placed along the edges of the grid.
        #This code works by initializing "edges", a master list that holds 
        #lists of coordinates generated by iterating all possible edge values 
        #starting from the corners.
        edges = (
        [(0, i) for i in range(self.grid_size)] +
        [(self.grid_size-1, i) for i in range(self.grid_size)] +
        [(i, 0) for i in range(self.grid_size)] +
        [(i, self.grid_size-1) for i in range(self.grid_size)]
        )

        #A coordinate in the edges set above is randomly assigned as an exit.
        self.exit_pos = random.choice(edges)
        
        return self.grid_size, self.player_pos, self.exit_pos, self.character
            
            

        
        