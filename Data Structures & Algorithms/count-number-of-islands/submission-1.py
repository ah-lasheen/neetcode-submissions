class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row: int, col: int):
            
            if row < 0 or col < 0 or row > len(grid) - 1 or col > len(grid[0]) - 1 or grid[row][col] != "1":
                return

            grid[row][col] = "0"

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
        
        total = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(row, col)
                    total += 1

        return total