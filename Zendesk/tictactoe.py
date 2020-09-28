def main():
    print("Welcome to TicTacToe!\n")
    choice, board = 1, None
    player1 = str(input("Enter name for Player 1:"))
    player2 = str(input("Enter name for Player 2:"))
    players = [player1, player2]
    while 0<choice<3:
        print("Please select from the following options below:\n"
              "1: Start new game & Set board size\n"
              "2: Play Game\n"
              "Other Entry: Quit game\n")
        choice = int(input("Your option:"))
        if choice == 1:
            board, size = initialise()
        elif choice == 2:
            if board is not None:
                board = play_game(board, size, players)
            else:
                print("Please select '1: Start new game & Set board size' first!")
        else:
            print("QUITTING GAME...")
    return

def initialise(size=2):
    if size < 3:
        print("Select a board size larger than 2. \n")
        size = int(input("Your board size:"))

    arr = [["-" for x in range(size+1)] for y in range(size+1)]
    arr[0] = [str(col_num) for col_num in range(size+1)]
    for row_num in range(size+1):
        arr[row_num][0]=row_num
    print("Your board is... \n")
    for b in range(size+1):
        print(arr[b])
    return arr, size

def checking(board, row, column, size, turn):
    """Checks NW, N, NE, E of the selected box, board[row][column] first,
    then checks corresponding the symmetrically opposite direction, SE, S, SW, W of the box"""
    back1_row = [row - 1, row - 1, row - 1, row]
    back1_col = [column - 1, column, column+1, column+1]
    back2_row = [row - 2, row - 2, row - 2, row]
    back2_col = [column - 2, column, column + 2, column + 2]
    fwd1_row = [row + 1, row + 1, row + 1, row]
    fwd1_col = [column + 1, column, column - 1, column - 1]
    fwd2_row = [row + 2, row + 2, row + 2, row]
    fwd2_col = [column + 2, column, column - 2, column - 2]
    "Above stores the directions and steps away from original box to check"
    prev_positive = [0 for ind in back1_row]
    """if 1 box in any direction has the same symbol, 
    we continue to check the next box in the same direction,
    or the symmentrically opposite box from the origin.
    """

    if turn == 1:
        symbol = "O"
    else:
        symbol = "X"

    for dir in range(4):
        check_row_oneback = back1_row[dir]  #Row of adjacent box to check
        check_col_oneback = back1_col[dir]  #Col of adjacent box to check
        if (check_row_oneback >= 0) and (check_row_oneback <= size) and (check_col_oneback >= 0) and (check_col_oneback <= size):
            if board[check_row_oneback][check_col_oneback] == symbol:
                prev_positive[dir] = 1
                check_row_twoback = back2_row[dir]  #Row of 2 adjacent box away to check
                check_col_twoback = back2_col[dir]  #Col of 2 adjacent box away to check
                if (check_row_twoback >= 0) and (check_row_twoback <= size) and (check_col_twoback >= 0) and (check_col_twoback <= size):
                    if (board[check_row_twoback][check_col_twoback] == symbol) & (prev_positive[dir] == 1):
                        return turn
        check_row_onefwd = fwd1_row[dir]    #Row of adjacent box in opposite direction to check
        check_col_onefwd = fwd1_col[dir]    #Col of adjacent box in opposite direction to check
        if (check_row_onefwd >= 0) and (check_row_onefwd <= size) and (check_col_onefwd >= 0) and (check_col_onefwd <= size):
            if board[check_row_onefwd][check_col_onefwd] == symbol:
                "if box in the opposite direction is already filled by same player"
                if prev_positive[dir] == 1:
                    return turn
                check_row_twofwd = fwd2_row[dir]    #Row of 2 adjacent box in opposite direction to check
                check_col_twofwd = fwd2_col[dir]    #Col of 2 adjacent box in opposite direction to check
                if (check_row_twofwd >= 0) and (check_row_twofwd <= size) and (check_col_twofwd >= 0) and (check_col_twofwd <= size):
                    if board[check_row_twofwd][check_col_twofwd] == symbol:
                        return turn
    return 0

def check_tie(board,size):
    for r in range(1,size+1):
        for c in range(1,size+1):
            if (board[r][c] != "O") & (board[r][c] != "X"):
                return 0
    print ("All boxes are filled!")
    return 1


def play_game(board, size, players):
    result, turn = 0, 1
    while (result == 0) & (check_tie(board,size) != 1):
        print(players[turn-1] + "'s turn!")
        print("Current board:")

        for b in range(size+1):
            print(board[b])

        row = int(input("Please input the row for your next move:"))
        column = int(input("Please input the column for your next move:"))
        while (row < 1)or(row > size)or(column < 1)or(column > size):
            print("OUT OF RANGE!")
            row = int(input("Please input the row for your next move:"))
            column = int(input("Please input the column for your next move:"))

        while (board[row][column] == "O") | (board[row][column] == "X"):
            row = int(input("The above box is occupied, select another row for your next move:"))
            column = int(input("The above box is occupied, select another column for your next move:"))
        if turn == 1:
            board[row][column] = "O"
        elif turn == 2:
            board[row][column] = "X"
        result = checking(board, row, column, size, turn)

        if turn == 1:
            turn = 2
        elif turn == 2:
            turn = 1
        else:
            print("Error")

    if check_tie(board,size):
        print("This game is a DRAW!")
    elif result:
        print(players[turn-1] + " has won!\n"
                                        "End Game Results:")
        for b in range(size+1):
            print(board[b])


    print("Clearing board, starting new game...")
    board, size = initialise(size)
    return board

main()
