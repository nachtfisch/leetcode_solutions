from collections import deque

class Solution:
    # dikstra or 1-0 bfs
    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque([(0,0,0)])
        seen = set((0,0))
        while q:
            c,x,y = q.popleft()            
            if x == m - 1 and y == n-1:
                return c
            seen.add((x,y))
            for dx, dy, sign in [(0,+1, 1), (+1, 0, 3), (0,-1, 2), (-1, 0 ,4)]:
                nx, ny = x + dx, y + dy
                if self._is_valid(nx, ny, m, n) and (nx,ny) not in seen:
                    if sign == grid[x][y]:
                        q.appendleft((c,nx, ny))
                    else:
                        q.append((c+1, nx, ny))
    
    def _is_valid(self, row, col, num_rows, num_cols) -> bool:
        return 0 <= row <= num_rows and 0 <= col < num_cols
