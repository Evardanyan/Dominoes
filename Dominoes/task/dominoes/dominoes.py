import random

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

while len(computer_pieces) != 7:
    num1 = random.randint(0, 6)
    num2 = random.randint(0, 6)
    if [num1, num2] not in computer_pieces:
        computer_pieces.append([num1, num2])

while len(player_pieces) != 6:
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

#----------------------------------------------------------------------

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
    status = "player"
else:
    domino_snake = max_player
    status = "computer"


print(f"Stock pieces: {stock_pieces}")
print(f"Computer pieces: {computer_pieces}")
print(f"Player pieces: {player_pieces}")
print(f"Domino snake: [{domino_snake}]")
print(f"Status: {status}")