class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowl, rowr, rowlast = 0, len(matrix) - 1, len(matrix[0]) - 1
        
        while rowl <= rowr:
            rowm = (rowl + rowr) // 2

            if target < matrix[rowm][0]:
                rowr = rowm - 1
            elif target > matrix[rowm][rowlast]:
                rowl = rowm + 1
            else:
                # put 2nd binary search
                l, r, row = 0, rowlast, matrix[rowm]

                while l <= r:
                    m = (l + r) // 2

                    if row[m] == target:
                        return True
                    elif row[m] < target:
                        l = m + 1
                    else:
                        r = m - 1

                return False

        return False