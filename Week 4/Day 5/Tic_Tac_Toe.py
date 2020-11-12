checks = {"1,1": " ", "1,2": " ", "1,3": " ",
            "2,1": " ", "2,2": " ", "2,3": " ",
            "3,1": " ", "3,2": " ", "3,3": " "}

def display_board():
    print("\n\n")
    print("*"*17)
    print(f"*   {checks['1,1']} | {checks['1,2']} | {checks['1,3']}   *")
    print("*  ---|---|---  *")
    print(f"*   {checks['2,1']} | {checks['2,2']} | {checks['2,3']}   *")
    print("*  ---|---|---  *")
    print(f"*   {checks['3,1']} | {checks['3,2']} | {checks['3,3']}   *")
    print("*"*17)


def player_input(player):
    input_validity = False
    while input_validity == False:
        coordinates = input(f"Player {player}'s move (e.g. '1,2'): ")
        input_validity = check_input(coordinates)

    return coordinates



def check_input(coordinates):
    if (coordinates[0] not in "123") or (coordinates[2] not in "123"):
        print("Entry is invalid")
        return False
    if (coordinates[0] not in "123") and (coordinates[2] not in "123"):
        print("Entry is invalid")
        return False
    if checks[coordinates] != " ":
        print("Entry is invalid")
        return False
    return coordinates



def check_win():
    #cols
    for col in range(1, 4):
        if checks[f"1,{col}"] == checks[f"2,{col}"] == checks[f"3,{col}"] != " ":
            return checks[f"1,{col}"]
    #rows
    for row in range(1, 4):
        if checks[f"{row},1"] == checks[f"{row},2"] == checks[f"{row},3"] != " ":
            return checks[f"{col},1"]
    #across
    if checks["1,1"] == checks["2,2"] == checks["3,3"] != " ":
        return checks["1,1"]
    if checks["3,1"] == checks["2,2"] == checks["1,3"] != " ":
        return checks["3,1"]
    
    #check for draw
    if " " not in checks.values():
        return "draw"
    return False



def play():
    win = False
    player1 = "X"
    player2 = "O"

    # collect inputs
    while True:
        display_board()
        player1_coord = player_input(player1)
        checks[player1_coord] = player1
        win = check_win()
        if win != False:
            break
        display_board()
        player2_coord = player_input(player2)
        checks[player2_coord] = player2
        win = check_win()
        if win != False:
            break
    display_board()
    if win == "draw":
        print("It's a draw!")
    else:
        print(f"{win} wins the game!")