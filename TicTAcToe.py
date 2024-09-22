def init_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def check_winner(board, player):
    for row in board:
        if row.count(player) == 3:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return best_score

def best_move(board):
    best_score = float('-inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def human_move(board):
    while True:
        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter column (0, 1, 2): "))
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            board[row][col] = 'X'
            break
        else:
            print("Invalid move, try again.")

def play_game():
    board = init_board()
    print_board(board)
    
    while True:
        # Human move
        human_move(board)
        print_board(board)
        if check_winner(board, 'X'):
            print("You win!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break
        
        move = best_move(board)
        board[move[0]][move[1]] = 'O'
        print("AI move:")
        print_board(board)
        if check_winner(board, 'O'):
            print("AI wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

play_game()
