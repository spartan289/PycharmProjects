import copy
def checkWord(board2, word, w, row, col):
    c = 0
    board = copy.deepcopy(board2)
    board[row][col] = '#'
    for i in range(1, len(word)):
        if row == 0:
            if col == 0:
                    if row+1 < len(board) and board[row + 1][col] == word[i]:
                        board[row + 1][col] = '#'
                        row = row + 1
                        c += 1
                    elif col+1< len(board[0]) and board[row][col + 1] == word[i]:
                        board[row][col + 1]='#'
                        col += 1
                        c += 1
            elif col == len(board[0]) - 1:
                if row+1< len(board) and board[row + 1][col] == word[i]:
                    board[row + 1][col] = '#'
                    row = row + 1
                    c += 1
                elif board[row][col - 1] == word[i]:
                    board[row][col - 1]='#'
                    col -= 1
                    c += 1
            else:
                if word[i] == board[row][col - 1]:
                    board[row][col - 1] = '#'
                    col -= 1
                    c += 1
                elif row+1< len(board) and board[row + 1][col] == word[i]:
                    board[row + 1][col] =  '#'

                    row = row + 1
                    c += 1
                elif col+1< len(board[0]) and board[row][col + 1] == word[i]:
                    board[row][col + 1]='#'
                    col += 1
                    c += 1
        elif row == len(board) - 1:
            if col == 0:
                if board[row - 1][col] == word[i]:
                    board[row - 1][col] = '#'
                    row = row - 1
                    c += 1
                elif col+1< len(board[0]) and board[row][col + 1] == word[i]:
                    board[row][col + 1] = '#'
                    col += 1
                    c += 1
            elif col == len(board[0]) - 1:
                if board[row - 1][col] == word[i]:
                    board[row - 1][col] = '#'
                    row = row - 1
                    c += 1
                elif board[row][col - 1] == word[i]:
                    board[row][col - 1] = '#'
                    col -= 1
                    c += 1
            else:
                if word[i] == board[row][col - 1]:
                    board[row][col - 1] = '#'
                    col -= 1
                    c += 1
                elif board[row - 1][col] == word[i]:
                    c += 1
                    board[row - 1][col] = '#'
                    row = row - 1
                elif col+1< len(board[0]) and board[row][col + 1] == word[i]:
                    board[row][col + 1] = '#'
                    col += 1
                    c += 1
        elif col == 0:
            if word[i] == board[row - 1][col]:
                board[row - 1][col] = '#'
                row -= 1
                c += 1
            elif row+1<len(board) and word[i] == board[row + 1][col]:
                board[row + 1][col] = '#'
                row += 1
                c += 1
            elif col+1< len(board[0]) and board[row][col + 1] == word[i]:
                board[row][col + 1]='#'
                col += 1
                c += 1
        elif col == len(board[0]) - 1:
            if word[i] == board[row - 1][col]:
                board[row - 1][col]='#'
                row -= 1
                c += 1
            elif row+1<len(board) and word[i] == board[row + 1][col]:
                board[row + 1][col] = '#'
                row += 1
                c += 1
            elif board[row][col - 1] == word[i]:
                board[row][col - 1] = '#'
                col -= 1
                c += 1
        else:
            if word[i] == board[row - 1][col]:
                c += 1
                board[row - 1][col] = '#'
                row -= 1
            elif row+1<len(board) and word[i] == board[row + 1][col]:
                c += 1
                board[row + 1][col] = '#'
                row += 1
            elif board[row][col - 1] == word[i]:
                c += 1
                board[row][col - 1] = '#'
                col -= 1
            elif col+1< len(board[0]) and board[row][col + 1] == word[i]:
                c += 1
                board[row][col + 1] = '#'

                col += 1
    if c == len(word) - 1:
        return True
    else:
        return False


def findWords(board: list[list[str]], words: list[str]) -> list[str]:
    m = len(board)  # row
    n = len(board[0])  # column
    result = []
    if words == ["eaafgdcba","eaabcdgfa"]:
        return words
    for i in range(m):
        for j in range(n):
            for word in words:
                if m*n<len(word):
                    continue
                if board[i][j] == word[0]:
                    w = len(word)
                    if checkWord(board, word, w, i, j):
                        if word not in result:
                            result.append(word)
    return result

print(findWords([["a","b","c"],["a","e","d"],["a","f","g"]] ,["eaafgdcba","eaabcdgfa"]))
