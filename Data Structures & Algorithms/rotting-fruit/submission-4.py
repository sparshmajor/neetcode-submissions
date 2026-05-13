class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        NR = len(grid)
        NC = len(grid[0])
        DC = [(1,0),(-1,0),(0,1),(0,-1)]
        q =[]
        fresh =0
        # visited = [[False]*NC for i in range(NR)]
        visited = set()
        for row in range(NR):
            for col in range(NC):
                if grid[row][col] == 2:
                    q.append((row,col))
                    # visited[row][col] = True
                    visited.add((row,col))
                if grid[row][col] == 1:
                    fresh +=1    
        step =0
        flag =0
        
        def check(r,c):
            nonlocal flag
            nonlocal fresh
            print(r,c)
            if r >= NR or c >= NC or r < 0 or c <0 or ((r,c) in visited):
                print("returning")
                return 
            if grid[r][c] == 1:
                print("appended")
                q.append((r,c)) 
                grid[r][c] = 2
                flag =1
                fresh -=1

            # visited[nr][nc] = True
            visited.add((nr,nc))    

        while len(q) > 0 and fresh >0:
            flag =0
            for _ in range(len(q)):
                print("q",q)
                print("visisted", visited)
                row,col = q.pop(0)
                for dr,dc in DC:
                    nr,nc = row+dr, col+dc
                    check(nr,nc)
                
            if flag:
                step+=1

                print("step", step) 
        if fresh == 0:
            return step
        else:
            return -1         








        