import sys
# sys.setrecursionlimit(50)

n = int(input())

board = [[0 for _ in range(n)] for _ in range(n)]
l = len(board)

def safety(board, x, y):
    l = len(board)
    if 1 in map(lambda x: x[y], board) or 1 in board[x]:
        return False
    
    for i in range(l):
        if i <= y:
            if i <= x:
                if board[x-i][y-i]:
                    return False
            if i+x < l:
                if board[x+i][y-i]:
                    return False
    return True


def queens(l=l, col=0):
    global board

    if col == l:
        return board
    for row in range(l):
        if board[row][col]:
            board[row][col] = 0
            continue

        if safety(board, row, col):
            board[row][col] = 1
            return queens(col=col+1)
    return queens(col=col-1)


def main():
    queens()
    for row in board:
        for i in row:
            print(i, end=' ')
        print()

if __name__ == "__main__":
    main()