board = {
    'U1' : ' ', 'U2' : ' ', 'U3' : ' ',
    'M1' : ' ', 'M2' : ' ', 'M3' : ' ',
    'L1' : ' ', 'L2' : ' ', 'L3' : ' '}


player = 1           #to initialise first player
total_moves = 0      #to count the moves

print("u1|U2|U3")
print("- +- +-")
print("M1|M2|M3")
print("- +- +-")
print("L1|L2|L3")
print("**********************")

while True:
    print(board['U1']+'|'+board['U2']+'|'+board['U3'])
    print('-+-+-')
    print(board['M1']+'|'+board['M2']+'|'+board['M3'])
    print('-+-+-')
    print(board['L1']+'|'+board['L2']+'|'+board['L3'])
    if total_moves == 9:
        break
    while True:             #input from players
        if player == 1:    #choose player
            p1_input = input('Player one')
            if p1_input.upper() in board and board[p1_input.upper()] ==' ':
                board[p1_input.upper()] = 'X'
                player = 2
                break
            else:
                print("Invalid input,please try again")
                continue
        else:
            p2_input = input('player two')
            if p2_input.upper() in board and board[p2_input.upper()] == ' ':
                board[p2_input.upper()] = '0'
                player = 1
                break
            else:      #on wrong input
                print("Invalid input,please try again")
                continue
    total_moves += 1
    print("**************************")
    print()
