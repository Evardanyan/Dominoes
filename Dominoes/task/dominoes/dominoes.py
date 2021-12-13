import random
from collections import deque

# stock_pieces = {}
stock_pieces = []
computer_pieces = []
player_pieces = []

computer_pieces_double_filter = []
player_pieces_double_filter = []

status = ""
max_computer = [0, 0]
max_computer_temp = 0
max_player = [0, 0]
max_player_temp = 0
domino_snake = []
temp_player_sum = 0
temp_computer_sum = 0

while len(stock_pieces) != 14:
    num1 = random.randint(0, 6)
    num2 = random.randint(0, 6)
    if [num1, num2] not in stock_pieces:
        stock_pieces.append([num1, num2])

# while True:
#     if len(player_pieces_double_filter) > 0 or len(computer_pieces_double_filter) > 0:
#         break
# ------------------------------working solution--------------------------------
# random_pieces = random.randint(6, 7)
# if random_pieces == 7:
#     computer_pieces_count = random_pieces
#     player_pieces_count = random_pieces - 1
# if random_pieces == 6:
#     computer_pieces_count = random_pieces
#     player_pieces_count = random_pieces + 1
#
# while len(computer_pieces) != computer_pieces_count:
#     num1 = random.randint(0, 6)
#     num2 = random.randint(0, 6)
#     if [num1, num2] not in computer_pieces:
#         computer_pieces.append([num1, num2])
#
# while len(player_pieces) != player_pieces_count:
#     num1 = random.randint(0, 6)
#     num2 = random.randint(0, 6)
#     if [num1, num2] not in player_pieces:
#         player_pieces.append([num1, num2])
# ------------------------------------------------------------

while len(computer_pieces) != 7:
    num1 = random.randint(0, 6)
    num2 = random.randint(0, 6)
    if [num1, num2] not in computer_pieces:
        computer_pieces.append([num1, num2])

while len(player_pieces) != 7:
    num1 = random.randint(0, 6)
    num2 = random.randint(0, 6)
    if [num1, num2] not in player_pieces:
        player_pieces.append([num1, num2])

for i, j in computer_pieces:
    temp_computer_sum = i + j
    # print(temp_computer_sum)
    if max_computer_temp < temp_computer_sum:
        max_computer_temp = temp_computer_sum
        max_computer = [i, j]

# print(computer_pieces_double_filter)

for i, j in player_pieces:
    temp_player_sum = i + j
    # print(temp_computer_sum)
    if max_player_temp < temp_player_sum:
        max_player_temp = temp_player_sum
        max_player = [i, j]

    # print(stock_pieces)
    # print(computer_pieces)
    # print(player_pieces)
# ------------------------DOuble checking -----------------------------
# for i, j in computer_pieces:
#     if i == j:
#         computer_pieces_double_filter.append([i, j])
#
# # print(computer_pieces_double_filter)
#
# for i, j in player_pieces:
#     if i == j:
#         player_pieces_double_filter.append([i, j])

# ----------------------------------------------------------------------

# print(player_pieces_double_filter)

# for i in computer_pieces_double_filter:
#     if max_computer < i:
#         max_computer = i
#
# for i in player_pieces_double_filter:
#     if max_player < i:
#         max_player = i

if max_computer > max_player:
    domino_snake = max_computer
    computer_pieces.remove(max_computer)
    status = "player"
else:
    domino_snake = max_player
    player_pieces.remove(max_player)
    status = "computer"

# ----------------first stage output----------------------
# print(f"Stock pieces: {stock_pieces}")
# print(f"Computer pieces: {computer_pieces}")
# print(f"Player pieces: {player_pieces}")
# print(f"Domino snake: [{domino_snake}]")
# print(f"Status: {status}")
# --------------------------------------------------------
# if status == "computer":
#     print('The Computer makes the first move (status = "computer")')
# else:
#     print('The player makes the first move (status = "player")')
# print()
# print("======================================================================")
queue = deque()
queue.appendleft(domino_snake)


def print_result():
    print(70 * "=")
    print(f"Stock size: {len(stock_pieces)}")
    print(f"Computer pieces: {len(computer_pieces)}")
    print()
    print("testing", queue)
    # print(f"{domino_snake}")
    if len(queue) < 7:
        for n in list(queue):
            print(n, end="")
    else:
        print(f"{queue[0]} {queue[1]} {queue[2]} ... {queue[-3]} {queue[-2]} {queue[-1]}")
    print()
    print()
    print("Your pieces:")
    # ----------------Your pieces---------------------
    j = 1
    for i in player_pieces:
        print(f"{j}:{i}")
        j += 1
    # ------------------------------------------------
    print()


# print_result()
# if status == "computer":
#     print("Status: Computer is about to make a move. Press Enter to continue...")
# else:
#     print("Status: It's your turn to make a move. Enter your command.")


if status == "computer":
    while True:
        if len(computer_pieces) == 0:
            print_result()
            break
            print("Status: The game is over. The computer won!")
        if len(player_pieces) == 0:
            print_result()
            print("Status: The game is over. You won!")
            break
        print_result()
        print("Status: Computer is about to make a move. Press Enter to continue...")
        num_computer = random.randint(-len(computer_pieces), len(computer_pieces))
        if num_computer == 0 and len(stock_pieces) != 0:
            computer_pieces.append(stock_pieces.pop())
        elif num_computer < 0:
            queue.appendleft(computer_pieces[num_computer])
            computer_pieces.pop(abs(num_computer) - 1)
        else:
            queue.append(computer_pieces[num_computer])
            computer_pieces.pop(abs(num_computer) - 1)
        print_result()
        print("Status: It's your turn to make a move. Enter your command.")
        while True:
            num_player = input()
            if num_player.isdigit():
                num_player = int(num_player)
                break
            else:
                print("Invalid input. Please try again.")
        if num_player == 0 and len(stock_pieces) != 0:
            player_pieces.append(stock_pieces.pop())
        elif num_player < 0:
            queue.appendleft(player_pieces[abs(num_player)])
            player_pieces.pop(abs(num_player) - 1)
        else:
            queue.append(player_pieces[abs(num_player)])
            player_pieces.pop(abs(num_player) - 1)

else:
    while True:
        if len(computer_pieces) == 0:
            print_result()
            break
            print("Status: The game is over. The computer won!")
        if len(player_pieces) == 0:
            print_result()
            print("Status: The game is over. You won!")
            break
        print_result()
        print("Status: It's your turn to make a move. Enter your command.")
        while True:
            num_player = input()
            if num_player.isdigit():
                num_player = int(num_player)
                break
            else:
                print("Invalid input. Please try again.")
        if num_player == 0 and len(stock_pieces) != 0:
            player_pieces.append(stock_pieces.pop())
        elif num_player < 0:
            queue.appendleft(player_pieces[abs(num_player)])
            player_pieces.pop(abs(num_player) - 1)
        else:
            queue.append(player_pieces[abs(num_player)])
            player_pieces.pop(abs(num_player) - 1)
        print_result()
        print("Status: Computer is about to make a move. Press Enter to continue...")
        num_computer = random.randint(-len(computer_pieces), len(computer_pieces))
        if num_computer == 0 and len(stock_pieces) != 0:
            computer_pieces.append(stock_pieces.pop())
        if num_computer < 0:
            queue.appendleft(computer_pieces[num_computer])
            computer_pieces.pop(abs(num_computer) - 1)
        else:
            queue.append(computer_pieces[num_computer])
            computer_pieces.pop(abs(num_computer) - 1)

# ------------------------------------------------
