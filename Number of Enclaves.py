class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        self.grid = grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i == 0 or j == 0 or i == len(self.grid) - 1 or j == len(self.grid[0]) - 1) and self.grid[i][j] == 1:
                    self.check_sea(i, j)
        return sum(sum(self.grid, []))

    def check_sea(self, a, b):
        if a == -1 or b == -1 or a == len(self.grid) or b == len(self.grid[0]) or self.grid[a][b] == 0:
            return
        self.grid[a][b] = 0
        self.check_sea(a, b - 1)
        self.check_sea(a - 1, b)
        self.check_sea(a + 1, b)
        self.check_sea(a, b + 1)


print(Solution().numEnclaves(grid=[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))
print(Solution().numEnclaves(grid=[[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]))
print(Solution().numEnclaves(grid=[[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0,0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1,1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,1]]))