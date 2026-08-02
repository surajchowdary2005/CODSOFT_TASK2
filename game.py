import math

# ----------------------------
# Functions
# ----------------------------

def print_positions():
    print("\nBoard Positions")
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9")
    print()


def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


def check_winner(player):
    winning_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for combo in winning_positions:
        if all(board[i] == player for i in combo):
            return True

    return False


def is_draw():
    return " " not in board


# ----------------------------
# Minimax AI
# ----------------------------

def minimax(is_maximizing):

    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if is_draw():
        return 0

    if is_maximizing:

        best_score = -math.inf

        for i in range(9):

            if board[i] == " ":

                board[i] = "O"

                score = minimax(False)

                board[i] = " "

                best_score = max(score, best_score)

        return best_score

    else:

        best_score = math.inf

        for i in range(9):

            if board[i] == " ":

                board[i] = "X"

                score = minimax(True)

                board[i] = " "

                best_score = min(score, best_score)

        return best_score


def ai_move():

    best_score = -math.inf
    best_move = -1

    print("\n🤖 AI's Turn...")

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"


def player_move():

    while True:

        try:

            print("\n👤 Your Turn")
            move = int(input("Enter your move (1-9): "))

            if move < 1 or move > 9:
                print("❌ Please enter a number between 1 and 9.")
                continue

            if board[move-1] != " ":
                print("❌ That position is already taken.")
                continue

            board[move-1] = "X"
            break

        except ValueError:
            print("❌ Please enter numbers only.")


# ----------------------------
# Main Program
# ----------------------------

print("=" * 35)
print("      TIC-TAC-TOE AI")
print("      Human vs Computer")
print("=" * 35)

while True:

    board = [" " for _ in range(9)]

    print_positions()

    while True:

        print_board()

        player_move()

        if check_winner("X"):
            print_board()
            print("🎉 Congratulations! You Win!")
            break

        if is_draw():
            print_board()
            print("🤝 It's a Draw!")
            break

        ai_move()

        if check_winner("O"):
            print_board()
            print("🤖 AI Wins!")
            break

        if is_draw():
            print_board()
            print("🤝 It's a Draw!")
            break

    choice = input("\nDo you want to play again? (y/n): ").lower()

    if choice != "y":
        print("\nThank you for playing! 👋")
        break