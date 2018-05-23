#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 11
# Problem 3
# 204111 SEC 001

def main():
    board = [[4,9,2],[3,5,7],[8,1,6]]
    print(is_magic_square(board))

def is_magic_square(board):
    #Check Dupp
    check_board = []
    for z in range(len(board)):
        check_board.extend(board[z])
    seen = []
    for number in check_board:
        if number in seen:
            return False
        if number > len(board)**2 or number < 1:
            return False
        else:
            seen.append(number)

    #Check column
    compare = 0
    for i in range(len(board)):
        for j in range(len(board)):
            compare += (board[j][i])
        if compare != sum(board[0]):
            return False
        compare=0
        
    #Check row
    for i in range(len(board)):
        compare = sum(board[i])
        if compare != sum(board[0]):
            return False

    #Check diag
    compare = 0
    for i in range(len(board)):
        compare += board[i][i]
    if compare != sum(board[0]):
        return False

    #Check another diag
    compare = 0
    for i in range(len(board)):
        compare += board[i][len(board)-1-i]
    if compare != sum(board[0]):
        return False



    return True




if __name__ == '__main__':
    main()