class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        rl, rr = 0, len(matrix) - 1
        while rl <= rr:
            rm = (rl + rr) // 2
            if matrix[rm][0] <= target <= matrix[rm][-1]:
                row = matrix[rm]
                l, r = 0, len(row) - 1
                while l <= r:
                    m = (l + r) // 2
                    if row[m] == target:
                        return True
                    elif row[m] < target:
                        l = m + 1
                    else:
                        r = m - 1
                return False
            elif matrix[rm][0] < target:
                rl = rm + 1
            else:
                rr = rm - 1
        return False