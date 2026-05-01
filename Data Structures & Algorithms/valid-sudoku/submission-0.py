class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        # make tuples for the key of indicies of the grid: i.e -> (0,1) middle left grid
        matrix = {}

        # for each row
        for i in range(len(board)):
            # for each col
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    # set to rows: key = row, value = num in that row
                    # initialize default sets of values for rows and cols
                    curr_row = rows.setdefault(i, set())
                    curr_col = cols.setdefault(j, set())
                    curr_matrix = matrix.setdefault((i//3, j//3), set())
                    # if curr row or col is in respective sets, return false since violation
                    if board[i][j] in curr_row: return False
                    if board[i][j] in curr_col: return False
                    if board[i][j] in curr_matrix: return False
                    # if not false, add vals to set
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    matrix[(i//3,j//3)].add(board[i][j])

        return True