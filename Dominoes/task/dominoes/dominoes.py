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

# while len(stock_pieces) != 14:
#     num1 = random.randint(0, 6)
#     num2 = random.randint(0, 6)
#     if [num1, num2] not in stock_pieces:
#         stock_pieces.append([num1, num2])

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
    if [num1, num2] not in computer_pieces and [num1, num2] not in player_pieces:
        computer_pieces.append([num1, num2])

while len(player_pieces) != 7:
    num1 = random.randint(0, 6)
    num2 = random.randint(0, 6)
    if [num1, num2] not in player_pieces and [num1, num2] not in computer_pieces:
        player_pieces.append([num1, num2])

while len(stock_pieces) != 14:
    num1 = random.randint(0, 6)
    num2 = random.randint(0, 6)
    if [num1, num2] not in stock_pieces and [num1, num2] not in computer_pieces and [num1, num2] not in player_pieces:
        stock_pieces.append([num1, num2])

for i_player, j in computer_pieces:
    temp_computer_sum = i_player + j
    # print(temp_computer_sum)
    if max_computer_temp < temp_computer_sum:
        max_computer_temp = temp_computer_sum
        max_computer = [i_player, j]

# print(computer_pieces_double_filter)

for i_player, j in player_pieces:
    temp_player_sum = i_player + j
    # print(temp_computer_sum)
    if max_player_temp < temp_player_sum:
        max_player_temp = temp_player_sum
        max_player = [i_player, j]

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
    # print(stock_pieces)
    print(f"Computer pieces: {len(computer_pieces)}")
    print()
    # print("testing", queue)
    # print(f"{domino_snake}")
    if len(queue) < 6:
        for n in list(queue):
            print(n, end="")
    else:
        print(f"{queue[0]} {queue[1]} {queue[2]}...{queue[-3]} {queue[-2]} {queue[-1]}")
    print()
    print()
    print("Your pieces:")
    # ----------------Your pieces---------------------
    j = 1
    for i in player_pieces:
        print(f"{j}: {i}")
        j += 1
    # ------------------------------------------------
    print()


# print_result()
# if status == "computer":
#     print("Status: Computer is about to make a move. Press Enter to continue...")
# else:
#     print("Status: It's your turn to make a move. Enter your command.")
#-------------------------------------------------------------------------------------
# def computer_start():
#     global num_computer, num_player
#     while True:
#         if len(computer_pieces) == 0:
#             print_result()
#             print("Status: The game is over. The computer won!")
#             break
#         if len(player_pieces) == 0:
#             print_result()
#             print("Status: The game is over. You won!")
#             break
#         print_result()
#         print("Status: Computer is about to make a move. Press Enter to continue...")
#         print()
#         # print_result()
#         num_computer = random.randint(-len(computer_pieces), len(computer_pieces))
#         if num_computer == 0 and len(stock_pieces) != 0:
#             computer_pieces.append(stock_pieces.pop())
#         elif num_computer < 0:
#             queue.appendleft(computer_pieces[abs(num_computer) - 1])
#             computer_pieces.pop(abs(num_computer) - 1)
#         else:
#             queue.append(computer_pieces[abs(num_computer) - 1])
#             computer_pieces.pop(abs(num_computer) - 1)
#         print_result()
#         print("Status: It's your turn to make a move. Enter your command.")
#         while True:
#             num_player = input()
#             if num_player.isdigit():
#                 num_player = int(num_player)
#                 if num_player <= len(player_pieces):
#                     break
#                 else:
#                     print("Status: It's your turn to make a move. Enter your command.")
#             else:
#                 print("Invalid input. Please try again.")
#         print_result()
#         if num_player == 0 and len(stock_pieces) != 0:
#             player_pieces.append(stock_pieces.pop())
#         elif num_player < 0:
#             queue.appendleft(player_pieces[abs(num_player - 1)])
#             player_pieces.pop(abs(num_player) - 1)
#         else:
#             queue.append(player_pieces[abs(num_player - 1)])
#             player_pieces.pop(abs(num_player) - 1)
#
#
# def player_start():
#     global num_player, num_computer
#     while True:
#         if len(computer_pieces) == 0:
#             print_result()
#             print("Status: The game is over. The computer won!")
#             break
#         if len(player_pieces) == 0:
#             print_result()
#             print("Status: The game is over. You won!")
#             break
#         print_result()
#         print("Status: It's your turn to make a move. Enter your command.")
#         while True:
#             num_player = input()
#             if num_player.isdigit():
#                 num_player = int(num_player)
#                 if num_player <= len(player_pieces):
#                     break
#                 else:
#                     print("Status: It's your turn to make a move. Enter your command.")
#             else:
#                 print("Invalid input. Please try again.")
#         if num_player == 0 and len(stock_pieces) != 0:
#             player_pieces.append(stock_pieces.pop())
#         elif num_player < 0:
#             queue.appendleft(player_pieces[abs(num_player - 1)])
#             player_pieces.pop(abs(num_player) - 1)
#         else:
#             queue.append(player_pieces[abs(num_player - 1)])
#             player_pieces.pop(abs(num_player) - 1)
#         print_result()
#         print("Status: Computer is about to make a move. Press Enter to continue...")
#         print()
#         # print_result()
#         num_computer = random.randint(-len(computer_pieces), len(computer_pieces))
#         if num_computer == 0 and len(stock_pieces) != 0:
#             computer_pieces.append(stock_pieces.pop())
#         if num_computer < 0:
#             queue.appendleft(computer_pieces[abs(num_computer) - 1])
#             computer_pieces.pop(abs(num_computer) - 1)
#         else:
#             queue.append(computer_pieces[abs(num_computer) - 1])
#             computer_pieces.pop(abs(num_computer) - 1)
#
#
# if status == "computer":
#     # player_start()
#     computer_start()
# else:
#     # computer_start()
#     player_start()

# ------------------------------------------------
print_result()
while True:
#--------------new module for stage 4 snake start and end number-----------------------------
    # snake_start = queue[0][0]
    # snake_end = queue[-1][1]
    # print(f"snake start is {snake_start}")
    # print(f"snake end is {snake_end}")
    # print() # only for testing stage 4
    # print(queue,"\n") # only for testing stage 4
#------------------------------------------------------------------


    if len(computer_pieces) == 0:
        print_result()
        print("Status: The game is over. The computer won!")
        break
    elif len(player_pieces) == 0:
        print_result()
        print("Status: The game is over. You won!")
        break
    if status == "computer":
        # print_result()
        print("Status: Computer is about to make a move. Press Enter to continue...")
        enter_button = input()
        if len(computer_pieces) == 0:
            # print_result()
            print("Status: The game is over. The computer won!")
            break
        if enter_button == "":
            print()
            # print(f"computer pieces is {computer_pieces}")
            # print_result()
#---------------------------this module for stage 4 computers------------------------------------------------
            snake_start = queue[0][0]
            snake_end = queue[-1][1]
            computer_piece_rotate= []
#--------------------------this module for stage 5 AI for computer-------------------------------------------
            count = 0

            computer_pieces_convert_list = [item for sublist in computer_pieces for item in sublist]

            merged_computer_pieces_snake = computer_pieces_convert_list + domino_snake

            computer_pieces_with_domino_snake = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

            for i in merged_computer_pieces_snake:
                if i == 0:
                    count_zero = computer_pieces_with_domino_snake[0] + 1
                    computer_pieces_with_domino_snake[0] = count_zero
                elif i == 1:
                    count_one = computer_pieces_with_domino_snake[1] + 1
                    computer_pieces_with_domino_snake[1] = count_one
                elif i == 2:
                    count_two = computer_pieces_with_domino_snake[2] + 1
                    computer_pieces_with_domino_snake[2] = count_two
                elif i == 3:
                    count_three = computer_pieces_with_domino_snake[3] + 1
                    computer_pieces_with_domino_snake[3] = count_three
                elif i == 4:
                    count_four = computer_pieces_with_domino_snake[4] + 1
                    computer_pieces_with_domino_snake[4] = count_four
                elif i == 5:
                    count_five = computer_pieces_with_domino_snake[5] + 1
                    computer_pieces_with_domino_snake[5] = count_five
                elif i == 6:
                    count_six = computer_pieces_with_domino_snake[6] + 1
                    computer_pieces_with_domino_snake[6] = count_six


            # print(">>>>>> merged list with computer pieces is ", merged_computer_pieces_snake)

            # for k,v in computer_pieces_with_domino_snake.items():
            #     print(f"{k}: {v}")


            computer_pieces_count_sum = []

            for i in computer_pieces:
               computer_pieces_count_sum.append(computer_pieces_with_domino_snake[i[0]] + computer_pieces_with_domino_snake[i[1]])

            # print("computer_pieces is ", computer_pieces)
            #
            # print("computer pieces count sum is " , computer_pieces_count_sum)

            draw_flag_player = True
            for i in player_pieces:
                if i[0] == snake_start or i[0] == snake_end or i[1] == snake_start or i[1] == snake_end:
                    draw_flag_player = False
                    break
            flag = False
#--------------------------------- find solution for using max element then continue ------------------
            # max = 0

            computer_pieces_count_sum_temp = computer_pieces_count_sum

            # print("sum temp is", computer_pieces_count_sum_temp)

            while_flag = True

            while while_flag:

                # for j in computer_pieces_count_sum_temp:
                #     if j > max:
                #         max = j
                # if len(computer_pieces_count_sum_temp) != 0:
                max_element = max(computer_pieces_count_sum_temp)

                index_max_element = computer_pieces[computer_pieces_count_sum_temp.index(max_element)]

                # print("max is ", max_element)
                #
                # print("index is " , computer_pieces_count_sum_temp.index(max_element))



                if index_max_element[0] == snake_start or index_max_element[0] == snake_end or index_max_element[1] == snake_start or index_max_element[1] == snake_end:
                    flag = True

                    num_computer = index_max_element

                    i_computer = num_computer
                    # print(f"i_computer is {i_computer}")
                    computer_delete_num = computer_pieces.index(num_computer)
                    # for i in player_pieces:
                    if snake_start == i_computer[0]:
                        computer_piece_rotate = [i_computer[1], i_computer[0]]
                        # print(f"start and rotate {computer_piece_rotate}")
                        queue.appendleft(computer_piece_rotate)
                        computer_pieces.pop(computer_delete_num)
                        break
                    elif snake_start == i_computer[1]:
                        queue.appendleft(i_computer)
                        # print(f"start without rotate {i_computer}")
                        computer_pieces.pop(computer_delete_num)
                        break
                    elif snake_end == i_computer[0]:
                        queue.append(i_computer)
                        # print(f"end without rotate {i_computer}")
                        computer_pieces.pop(computer_delete_num)
                        break
                    elif snake_end == i_computer[1]:
                        computer_piece_rotate = [i_computer[1], i_computer[0]]
                        # print(f"end and rotate is {computer_piece_rotate}")
                        queue.append(computer_piece_rotate)
                        computer_pieces.pop(computer_delete_num)
                        break
                if len(computer_pieces_count_sum_temp) == 0 and len(stock_pieces) != 0:
                    computer_pieces.append(stock_pieces.pop())
                    # computer_pieces_count_sum_temp.remove(max_element)
                    while_flag = False
                    print("take from stock piece and out from  loop ")
                    break
                elif len(computer_pieces_count_sum_temp) != 0 and max_element != 0:
                    computer_pieces_count_sum_temp[computer_pieces_count_sum_temp.index(max_element)] = 0
                    # print(">>> len sum_temp_list after removed element",len(computer_pieces_count_sum_temp))
                    # print("removed max from sum list ")
                    # print(len(computer_pieces_count_sum_temp))

                elif max_element == 0 and len(stock_pieces) != 0:
                        computer_pieces.append(stock_pieces.pop())
                        # print("<<<<< max element is == 0 and stock pieces isnt 0", len(computer_pieces_count_sum_temp))
                        # print("removed max from sum list ")
                        # print(len(computer_pieces_count_sum_temp))
                        break
                # elif len(stock_pieces) != 0:
                #     computer_pieces.append(stock_pieces.pop())
                #     break
                elif len(stock_pieces) == 0 and len(player_pieces) != 0 and len(computer_pieces) != 0 and draw_flag_player:
                    print("Status: The game is over. It's a draw!")
                    break








#-------------------------------------------------------------------------------------------------------

#---------------------------Stage 4 solution for computer parts -----------------------------------------
            # for i in computer_pieces:
            #     # print(f"i[0] or i[1] is {i[0], i[1]}")
            #     if i[0] == snake_start or i[0] == snake_end or i[1] == snake_start or i[1] == snake_end:
            #         flag = True
            #         # print(f"i[0] or i[1] is {i[0],i[1]}")
            #         num_computer = i
            #         i_computer = num_computer
            #         # print(f"i_computer is {i_computer}")
            #         computer_delete_num = computer_pieces.index(num_computer)
            #         # for i in player_pieces:
            #         if snake_start == i_computer[0]:
            #             computer_piece_rotate = [i_computer[1], i_computer[0]]
            #             # print(f"start and rotate {computer_piece_rotate}")
            #             queue.appendleft(computer_piece_rotate)
            #             computer_pieces.pop(computer_delete_num)
            #             break
            #         elif snake_start == i_computer[1]:
            #             queue.appendleft(i_computer)
            #             # print(f"start without rotate {i_computer}")
            #             computer_pieces.pop(computer_delete_num)
            #             break
            #         elif snake_end == i_computer[0]:
            #             queue.append(i_computer)
            #             # print(f"end without rotate {i_computer}")
            #             computer_pieces.pop(computer_delete_num)
            #             break
            #         elif snake_end == i_computer[1]:
            #             computer_piece_rotate = [i_computer[1], i_computer[0]]
            #             # print(f"end and rotate is {computer_piece_rotate}")
            #             queue.append(computer_piece_rotate)
            #             computer_pieces.pop(computer_delete_num)
            #             break
            #
            # if flag == False and len(stock_pieces) != 0: # computer take dominos from stock
            #     computer_pieces.append(stock_pieces.pop())
            # elif flag == False and len(stock_pieces) == 0 and len(player_pieces) != 0 and len(computer_pieces) != 0 and draw_flag_player:
            #     print("Status: The game is over. It's a draw!")
            #     break
#-------------------------------------------stage  4 solution end part for computer ---------------------------------------------------------
            # i_computer = num_computer
            # computer_delete_num = computer_pieces.index(num_computer)
            # # for i in player_pieces:
            # if snake_start == i_computer[0]:
            #     computer_piece_rotate = [i_computer[1], i_computer[0]]
            #     print(f"start and roatate {computer_piece_rotate}")
            #     queue.appendleft(computer_piece_rotate)
            #     computer_pieces.pop(computer_delete_num)
            # elif snake_start == i_computer[1]:
            #     queue.appendleft(i_computer)
            #     print(f"start without rotate {i_computer}")
            #     computer_pieces.pop(computer_delete_num)
            # elif snake_end == i_computer[0]:
            #     queue.append(i_computer)
            #     print(f"end without rotate {i_computer}")
            #     computer_pieces.pop(computer_delete_num)
            # elif snake_end == i_computer[1]:
            #     player_piece_rotate = [i_computer[1], i_computer[0]]
            #     print(f"end and roatet is {computer_piece_rotate}")
            #     queue.append(computer_piece_rotate)
            #     computer_pieces.pop(computer_delete_num)





#--------------------------this module for stage 3 ----------------------------------------------------------
            # num_computer = random.randint(-len(computer_pieces), len(computer_pieces))
            # if num_computer == 0 and len(stock_pieces) != 0:
            #     computer_pieces.append(stock_pieces.pop())
            # elif num_computer < 0:
            #     queue.appendleft(computer_pieces[abs(num_computer) - 1])
            #     computer_pieces.pop(abs(num_computer) - 1)
            # else:
            #     queue.append(computer_pieces[abs(num_computer) - 1])
            #     computer_pieces.pop(abs(num_computer) - 1)
#---------------------------------------------------------------------------------------------------------
            # --------------new module for stage 4 snake start and end number-----------------------------
            # snake_start = queue[0][0]
            # snake_end = queue[-1][1]
            # print(f"snake start is {snake_start}")
            # print(f"snake end is {snake_end}")
            #---------------------------------------------------------------------------------------------
            status = "player"
            print_result()
    if status == "player":
        if len(computer_pieces) == 0:
            # print_result()
            print("Status: The game is over. The computer won!")
            break
        # print_result()
        snake_start = queue[0][0]
        snake_end = queue[-1][1]
        draw_flag_computer = True
        for i in computer_pieces:
            if i[0] == snake_start or i[0] == snake_end or i[1] == snake_start or i[1] == snake_end:
                draw_flag_computer = False
                break
        print("Status: It's your turn to make a move. Enter your command.")
        while True:
            try:
                i_player = -1
                num_player = abs(int(input()))
                # if abs(num_player) <= len(player_pieces):
                #     break
                if abs(num_player) <= len(player_pieces):
                    i_player = player_pieces[num_player - 1]
                    if num_player != 0 and (snake_start != i_player[0] and snake_start != i_player[1]) and (snake_end != i_player[0] and snake_end != i_player[1]):
                        print("Illegal move. Please try again.")
                    else:
                        break
                elif (num_player > len(player_pieces)):
                    print("Invalid input. Please try again.")
                    # print("Illegal move. Please try again.")
                else:
                    print("Status: It's your turn to make a move. Enter your command.")
            except ValueError:
                print("Invalid input. Please try again.")


#-----------------player module with any pieces on stage 3 deprected for stage 4--------------------

        # if num_player == 0 and len(stock_pieces) != 0:
        #     player_pieces.append(stock_pieces.pop())
        # elif num_player < 0:
        #     queue.appendleft(player_pieces[abs(num_player) - 1])
        #     player_pieces.pop(abs(num_player) - 1)
        # else:
        #     queue.append(player_pieces[abs(num_player) - 1])
        #     player_pieces.pop(abs(num_player) - 1)

#-------------------------------------------------------------------------------

        # --------------new module for stage 4 snake start and end number-----------------------------
        # snake_start = queue[0][0]
        # snake_end = queue[-1][1]
        # print(f"snake start is {snake_start}")
        # print(f"snake end is {snake_end}")
        # ---------------------------------------------------------------------------------------------
        #------------------------ new moduel for stage 4  put right piece of player and rotate it------
        # print(f"player pieces is {player_pieces}")
        # i_player = player_pieces[num_player - 1]
        # player_delete_num = num_player - 1
        # for i in player_pieces:
        if num_player == 0 and len(stock_pieces) != 0:
            player_pieces.append(stock_pieces.pop())
            status = "computer"
            # print_result()
        elif num_player == 0 and len(stock_pieces) == 0:
            print("Invalid input. Please try again.")
            # break

        elif num_player == 0 and len(stock_pieces) == 0 and len(player_pieces) != 0 and len(computer_pieces) != 0 and draw_flag_computer:
            print("Status: The game is over. It's a draw!")
            break
        else:
            # i_player = player_pieces[num_player - 1]
            player_delete_num = num_player - 1
            # if snake_start != i_player[0] and snake_start != i_player[1]:
            #     print("Illegal move. Please try again.")

            if snake_start == i_player[0]:
                player_piece_rotate = [i_player[1], i_player[0]]
                # print(f"start and roatate {player_piece_rotate}")
                queue.appendleft(player_piece_rotate)
                player_pieces.pop(player_delete_num)
            elif snake_start == i_player[1]:
                queue.appendleft(i_player)
                # print(f"start without rotate {i_player}")
                player_pieces.pop(player_delete_num)
            elif snake_end == i_player[0]:
                queue.append(i_player)
                # print(f"end without rotate {i_player}")
                player_pieces.pop(player_delete_num)
            elif snake_end == i_player[1]:
                player_piece_rotate = [i_player[1], i_player[0]]
                # print(f"end and roatet is {player_piece_rotate}")
                queue.append(player_piece_rotate)
                player_pieces.pop(player_delete_num)
        #----------------------------------------------------------------------------------------------
        status = "computer"
        print_result()


