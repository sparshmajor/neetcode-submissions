from collections import defaultdict
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS = len(heights)
        COLS = len(heights[0])
        DIR = [(0,1),(0,-1),(1,0),(-1,0)]
        res= [[float('inf')]*COLS for i in range(ROWS)]
        res[0][0] = 0
        # print(res)
        q=[]
        heapq.heappush(q, (0, (0,0)))
        while(q):
            dis, u = heapq.heappop(q)
            ux = u[0]
            uy = u[1]
            # print("ux, uy",ux, uy)
            for v in DIR:
                vx = ux + v[0]
                vy = uy + v[1]
                
                if 0 <= vx < ROWS and 0 <= vy < COLS:  
                    # print("vx, vy",vx, vy)
                    diff = max(dis, abs(heights[vx][vy]- heights[ux][uy]))
                    # print("diff",diff)
                    if res[vx][vy] > diff:
                        res[vx][vy] = diff
                        heapq.heappush(q, (diff, (vx,vy)))
                        # print("q",q)
                    # print("res", res)
                    # print("--------")    
        return res[ROWS-1][COLS-1]            





        