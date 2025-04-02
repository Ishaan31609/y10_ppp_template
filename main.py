### Guess counts initialisation ###

guess_counts_player_1 = 15
guess_counts_player_2 = 15

### Boolean values ###

allow_ship_movement_player_1 = False
allow_ship_movement_player_2 = False

### Tallying the correct guesses ###

correct_guess_player_1 = []
correct_guess_player_2 = []

### Status indicating whether game has ended ###

check_game_ended = False

### Initialising the 6 x 6 game board ###

def initialise_board ():

    return[["~"] * 6 for _ in range (6)]

### Game grid for player 1 ###

game_grid_player_1 = initialise_board()

### Game grid for player 2 ###

game_grid_player_2 = initialise_board()

### Selection Stage ###

def selection_ships(board, ship_size, ship_name):

    while True:
        print("\n Current Board: ") ### Showing this is the current board form ###
        print_board(board) ### Outputs the board ###
        print(f"Place your {ship_name} (size {ship_size}).") ### Informs the user that they will now have to place the different ships and also informs them of the ship size ###
        start_coordinates = input("Enter starting coordinates: (e.g. A1):   ") ### It is asking for one coordinate which will act as the pivot for the placement of the other coordinates according to validity ###

        try:
            start_x, start_y = convert_coordinates(start_coordinates) ### The x and y coordinates are going to store the starting coordinate values after the coordinates have been converted into list index form as a result of the convert_coordinates() function being called ###
        
        except ValueError as error: ### If there is an error. it will be stored in the variable error ###
            print(error) ### The error will be outputted to the user ###
            continue ### The rest of the program will continue as usual once there is no error in the input ###

        direction = input("Enter orientation (V if you would like to place it vertically) and (H if you would like to place it horizontally): ").upper() ### This line is demanding input from the player depending on whether they would like to place their ship vertically or horizontally. The user input is changed to uppercase ###

        if direction == "H" and start_x + ship_size <= 6: ### A conditional statement which is going to run if the user inputs H. It will only run if the ship will be able to fit in the grid ###

            if all(board[start_y][start_x + i] == "~" for i in range(ship_size)): ### The all() function returns a boolean depending on it's parameter. The parameter of the function is a validation method which makes sure the following square which will hold part of the ship is empty. ###
                for i in range (ship_size): ### The loop will repeat depending on how many grid spaces the ship takes (3, 2, 1)
                    board([start_y][start_x + i]) = "S" ### The board is being updated with the chaacter "S" standing for selected. The loop is going across the x-axis depending on the i value placing an "S" everytime. ###
            break ### Stopping the loop

        elif direction == "V" and start_y + ship_size <= 6: ### A conditional statement which is going to run if the user inputs H. It will only run if the ship will be able to fit in the grid ###

            if all(board[start_y + i][start_x] == "~" for i in range(ship_size)): ### The all() function returns a boolean depending on it's parameter. The parameter of the function is a validation method which makes sure the following square which will hold part of the ship is empty. ###
                for i in range (ship_size): ### The loop will repeat depending on how many grid spaces the ship takes (3, 2, 1) ###
                    board([start_y + i][start_x]) = "S" ### The board is being updated with the chaacter "S" standing for selected. The loop is going across the y-axis depending on the i value placing an "S" everytime. ###
            break ### Stopping the loop

        print("Invalid placement/input. Try again!!!") ### If there is invalid placement, the user will be notified.

### Board Printing Not Showing Ship Locations ###

def print_board(board, hide_ships = False): ### Defining the function print_board() ###
    print(" " + " ".join("A B C D E F".split())) ### Prints out column lables. The two spaces that are front are due to row positions ###
    for i, row in enumerate(board): ### By passing two variables in the for loop, we are avoiding writing 2 separate for loops. ### 
        if hide_ships: ### If the ships are to be hid ... ###
            print(f"{i + 1} " + " ".join("~" if cell == "S" else cell for cell in row)) ### Replaces any places with S to ~ to hide the selected positions
        else: ### Otherwise ...
            print(f"{i + 1} " + " ".join(row)) ### Print out board even if the locations are exposed ###

### Converting Coordinates - It converts user input into x and y coordinates ###

def convert_coordinates(coord):
    column = coord[0].upper() ### Assigning the variable column to the x-axis value in the coordinate, and also making it uppercase to be used later on ###
    row = coord[1] ### Assigning the row variable to y-axis value in the coordinate. ###
    if columnn in "ABCDEF" and row in "123456": ### Checking whether the input is in bounds ###
        x = ord(column) - ord("A") ### The ord() function finds the unicode value of the parameter. By subtracting the colum unicode number by the unicode value of "A" which is 65, we get the magnitude of the x-axis ###
        y = int(row) - 1 ### A string is converted into an integer and is subtracted by 1 to match python indexing ###
        return x, y ### x coordinate and y coordinates are returned ###

    else: ### Otherwise ... ###
        raise ValueError ("Invalid coordinate. Use format like A1 or F1.") ### The raise() function prints the output message when a value error occurs ###


### Get Guess Inputs From The Player ###

def get_guess(): 
    
    while True: 
        guess = input("Please enter bombing coordinates in the format A1: ") ### Asking for bombing coordinates input from user ###
        
        try: ### trying / testing code to check for errors ###
            return convert_coordinates(guess) ### The convert_coordinates() function is called and the variable guess is passed in it. An error here would show an error in guess input ###
            
        except ValueError as e: ### If there is an error, store the error message in variable e ###
            print(e) ### Output the error message ###

### Process The Bombing Coordinates ###

def process_guess(board, x, y):
    
    if board[y][x] == "S": ### Checking whether after the x and y coordinates have been applied, if the input matches the opponents ship location ###
        board[y][x] == "X" ### Setting that area on the board as X standing for hit ###
        print("HIT!!!") ### Outputting message HIT!!! ###
        return True ### Returning true as a ship has been hit ###

    elif board[y][x] == "~": ### Checking whether after the x and y coordinates have been applied, if the input does not match the opponents ship location ###
        board[y][x] == "O" ### Set that area on the board as O standing for miss ###
        print("MISS") ### Outputting message MISS ###
        return False ### Returning false as a ship has not been hit ###

    else: ### Otherwise ... ###
        print("Already guessed this coordinate. ") ### Outputting to the user that this coordinate has already been guessed ###
        return False ### Returning false as the guess was invalid ###

### Moving Large Ship Function ###

def move_large_ship(board):
    print("Move your large ship. ") ### Outputting to the user that access has been granted for ship movement ###
    for y in range(6): ### Looping through each row ###
        for x in range(6): ### Looping through each column ###
            if board[y][x] == "S": ### If at any part, a ship has been selected ###
                board[y][x] = "~" ### That area is replaced with ~ ###
 selection_ships(board, 3, "Large Ship") ### The selection_ships() function is being called and the board, ship size, and the name of the ship being passed into the function ###

### Checks whether the game is over ###

def check_game_over(board):
    return all(cell != "S" for row in board for cell in row) ### If there are no remaining cells with "S" then the game has ended as the "S" character is replaced with "X" if guessed correctly or "~" if the ship has been moved ###
    
### Main game loop ###

def play_game():

    print("Welcome to Moveable Ships! A Battleship Variant!") ### Outputting welcome message ###
    name_player_1 = input("What is your name player 1? : ") ### Storing player 1 name input ###
    name_player_2 = input("What is your name player 2? : ") ### Storing player 2 name input ###

    player_1_board = initialize_board() ### Initialising player 1 board ###
    player_2_board = initialize_board() ### Initialising player 2 board ###

    print(f"{name_player_1}, PLACE YOUR SHIPS.") ### Asserting player 1 by their name and letting them know that they now have to place their ships ###
    
    selection_ship(player_1_board, 3, "Large Ship") ### Calling selection_ship() function for large ship for player 1 ###
    selection_ship(player_1_board, 2, "Medium Ship") ### Calling selection_ship() function for medium ship for player 1 ###
    selection_ship(player_1_board, 1, "Small Ship") ### Calling selection_ship() function for small ship for player 1 ###

    print(f"{name_player_2}, PLACE YOUR SHIPS.") ### Asserting player 2 by their name and letting them know that they now have to place their ships ###
    
    selection_ship(player_2_board, 3, "Large Ship") ### Calling selection_ship() function for large ship for player 2 ###
    selection_ship(player_2_board, 2, "Medium Ship") ### Calling selection_ship() function for medium ship for player 2 ###
    selection_ship(player_2_board, 1, "Small Ship") ### Calling selection_ship() function for small ship for player 2 ###

    player_1_score = 0 ### Setting player 1 score to 0 ###
    player_2_score = 0 ### Setting player 2 score to 0 ###

    player_1_moves = 0 ### Setting player 1 moves to 0 ###
    player_2_moves = 0 ### Setting player 2 moves to 0 ###

    max_moves = 15 ### Setting the maximum number of moves allowed to 15 ###
