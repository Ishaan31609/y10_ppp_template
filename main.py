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