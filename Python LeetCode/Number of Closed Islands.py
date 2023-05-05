class Solution:
    def dfs(self, grid, i, j):
        # помечаем ячейку как посещенную
        grid[i][j] = 1
        # рекурсивно вызываем dfs для всех соседних ячеек
        if i > 0 and grid[i - 1][j] == 0:
            self.dfs(grid, i - 1, j)
        if i < len(grid) - 1 and grid[i + 1][j] == 0:
            self.dfs(grid, i + 1, j)
        if j > 0 and grid[i][j - 1] == 0:
            self.dfs(grid, i, j - 1)
        if j < len(grid[0]) - 1 and grid[i][j + 1] == 0:
            self.dfs(grid, i, j + 1)

    def closedIsland(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    # вызываем dfs для каждой непосещенной ячейки
                    self.dfs(grid, i, j)
                    # если ячейка не на границе сетки, то это замкнутый остров
                    if i > 0 and i < len(grid) - 1 and j > 0 and j < len(grid[0]) - 1:
                        count += 1
        return count

grid = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1],
        [1,0,1,1,1,0,1],
        [1,0,1,0,1,0,1],
        [1,0,1,1,1,0,1],
        [1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1]]

print(Solution().closedIsland(grid))
