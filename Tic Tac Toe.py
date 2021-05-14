board = {
    'U1' : ' ', 'U2' : ' ', 'U3' : ' ',
    'M1' : ' ', 'M2' : ' ', 'M3' : ' ',
    'L1' : ' ', 'L2' : ' ', 'L3' : ' '}


player = 1           #to initialise first player
total_moves = 0  #to count the moves
end_check = 0


def check():
    #checking moves of player 1
    #for horizontal start
    if board['U1'] == 'X' and board['U2'] == 'X' and board['U3'] == 'X':
        print("player one is the winner!!!")
        print("Game over!!!")
        return 1
    if board['M1'] == 'X' and board['M2'] == 'X' and board['M3'] == 'X':
        print("player one is the winner!!!")
        print("Game over!!!")
        return 1
    if board['L1'] == 'X' and board['L2'] == 'X' and board['L3'] == 'X':
        print("player one is the winner!!!")
        print("Game over!!!")
        return 1
    #for horizontal(end)
    #for diagonal start
    if board['U1'] == 'X' and board['M2'] == 'X' and board['L3'] == 'X':
        print("player one is the winner!!!")
        print("Game over!!!")
        return 1
    if board['U3'] == 'X' and board['M2'] == 'X' and board['L1'] == 'X':
        print("player one is the winner!!!")
        print("Game over!!!")
        return 1
     #for diagonal end
    #for vertical start
    if board['U1'] == 'X' and board['M1'] == 'X' and board['L1'] == 'X':
        print("player one is the winner!!!")
        print("Game over!!!")
        return 1
    if board['U2'] == 'X' and board['M2'] == 'X' and board['L2'] == 'X':
        print("player one is the winner!!!")
        print("Game over!!!")
        return 1
    if board['U3'] == 'X' and board['M3'] == 'X' and board['L3'] == 'X':
        print("player one is the winner!!!")
        print("Game over!!!")
        return 1
     #for vertical end

    #checking the moves of player two
     #for horizontal start
    if board['U1'] == '0' and board['U2'] == '0' and board['U3'] == '0':
        print("player two is the winner!!!")
        print("Game over!!!")
        return 1
    if board['M1'] == '0' and board['M2'] == '0' and board['M3'] == '0':
        print("player two is the winner!!!")
        return 1
    if board['L1'] == '0' and board['L2'] == '0' and board['L3'] == '0':
        print("player two is the winner!!!")
        print("Game over!!!")
        return 1
    #for horizontal(end)
    #for diagonal start
    if board['U1'] == '0' and board['M2'] == '0' and board['L3'] == '0':
        print("player two is the winner!!!")
        print("Game over!!!")
        return 1
    if board['U3'] == '0' and board['M2'] == '0' and board['L1'] == '0':
        print("player two is the winner!!!")
        print("Game over!!!")
        return 1
     #for diagonal end
    #for vertical start
    if board['U1'] == '0' and board['M1'] == '0' and board['L1'] == '0':
        print("player two is the winner!!!")
        print("Game over!!!")
        return 1
    if board['U2'] == '0' and board['M2'] == '0' and board['L2'] == '0':
        print("player two is the winner!!!")
        print("Game over!!!")
        return 1
    if board['U3'] == '0' and board['M3'] == '0' and board['L3'] == '0':
        print("player two is the winner!!!")
        print("Game over!!!")
        return 1
    return 0
     #for vertical end

    
    
print("U1|U2|U3")
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
    end_check = check()
    if total_moves == 9 and end_check == 0:
        print("it was a tie!!")
        print("Game over!!")
    if total_moves == 9 or end_check == 1:
        break
    while True:             #input from players
        if player == 1:    #choose player
            p1_input = input('Player one')
            if p1_input.upper() in board and board[p1_input.upper()] ==' ':
                board[p1_input.upper()] = 'X'
                player = 2
                break
            else:
                print("Invalid input!Try again!! ")
                continue
        else:
            p2_input = input('player two')
            if p2_input.upper() in board and board[p2_input.upper()] == ' ':
                board[p2_input.upper()] = '0'
                player = 1
                break
            else:      #on wrong input
                print("Invalid input!Try again")
                continue
            end_check = check()
    total_moves += 1
    print("**************************")
    print()
