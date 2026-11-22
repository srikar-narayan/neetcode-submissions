class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        sqr = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if board[i][j] in row[i]:
                    return False
                else:
                    row[i].add(board[i][j])

                if board[i][j] in col[j]:
                    return False
                else:
                    col[j].add(board[i][j])
                
                if board[i][j] in sqr[(i//3, j//3)]:
                    return False
                else:
                    sqr[(i//3, j//3)].add(board[i][j])
        return True
                