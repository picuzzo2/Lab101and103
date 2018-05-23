board = [[1,2,3,4],[5,6,7,8],[9,0]]
check_board = []
for z in range(len(board)):
    check_board.extend(board[z])
seen = []
for number in check_board:
    if number in seen:
        print(False)
        break
    else:
        seen.append(number)