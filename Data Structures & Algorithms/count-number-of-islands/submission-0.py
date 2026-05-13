class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count =0

        def dfs(grid, row, col):
            if row >= len(grid) or row < 0 or col >= len(grid[0]) or col <0 :
                return 0
            if grid[row][col] == "0":
                return 0    
            if (row, col) in visited:
                return 0      
            
            visited.add((row,col))
            dfs(grid, row+1, col)
            dfs(grid, row-1, col)
            dfs(grid, row, col+1)
            dfs(grid, row, col-1)
            
            return 1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += dfs(grid, row, col)
                    
        return count            





        