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

### Board Printing ###

def print_board(board):

### Main game loop ###

def main():
    
    name_player_1 = input("What is your name player 1? : ")
    name_player_2 = input("What is your name player 2? : ")