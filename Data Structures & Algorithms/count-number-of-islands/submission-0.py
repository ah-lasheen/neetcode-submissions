class Solution:
    def findAdjacent(self, row: int, col: int, grid: List[List[str]]) -> None:
        # base cases: out of bounds OR water/visited
        if (row < 0 or row >= len(grid) or
            col < 0 or col >= len(grid[0]) or
            grid[row][col] != "1"):
            return
        
        # mark this land cell as visited
        grid[row][col] = "0"
        
        # DFS in four directions
        self.findAdjacent(row - 1, col, grid)
        self.findAdjacent(row + 1, col, grid)
        self.findAdjacent(row, col - 1, grid)
        self.findAdjacent(row, col + 1, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:                # empty input guard
            return 0
                
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":   # found new island
                    self.findAdjacent(r, c, grid)
                    count += 1
        return count