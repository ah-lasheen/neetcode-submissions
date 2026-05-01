class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        matrix = {}

        # for each row
        for i in range(len(board)):
            # for each col
            for j in range(len(board[i])):
                val = board[i][j]
                if val != ".":  # Ignore empty cells
                    curr_row = rows.setdefault(i, set())
                    curr_col = cols.setdefault(j, set())
                    curr_matrix = matrix.setdefault((i//3, j//3), set())

                    if val in curr_row or val in curr_col or val in curr_matrix: return False

                    rows[i].add(val)
                    cols[j].add(val)
                    matrix[(i//3, j//3)].add(val)


        return True

