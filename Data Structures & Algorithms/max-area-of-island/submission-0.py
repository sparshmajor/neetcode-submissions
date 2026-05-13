class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res= 0
        visited = set()    
        def dfs(grid, row, col):
            if row >= len(grid) or col >= len(grid[0]) or row <0 or col <0:
                return 0

            if grid[row][col] == 0:
                return 0

            if (row, col) in visited:
                return 0
            visited.add((row,col))    
            count = 1
            count += dfs(grid,row-1,col)    
            count += dfs(grid,row+1,col)    
            count += dfs(grid,row,col-1)    
            count += dfs(grid,row,col+1)    
            return count

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, dfs(grid, i, j))  
        return res                  
        