def safety(board, x, y):
    l = len(board)
    if 1 in map(lambda x: x[y], board) or 1 in board[x]:
        print("threat at row or col")
        return False
    
    for i in range(l):
        if i <= y:
            if i <= x:
                if board[x-i][y-i]:
                    print(f"threat at {x-i}, {y-i}")
                    return False
            if i+x < l:
                if board[x+i][y-i]:
                    print(f"threat at {x+i}, {y-i}")
                    return False
    print("safe")
    return True

board = [
    [0 for _ in range(4)]
    for _ in range(4)
]

board[0][0] = 1
board[3][1] = 1

for row in board:
    print(row)

print()
print(safety(board, 1, 2))