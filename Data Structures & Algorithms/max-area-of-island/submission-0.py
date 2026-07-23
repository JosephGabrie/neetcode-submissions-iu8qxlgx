class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1],[0,-1]]
        seen = set()
        max_area = 0
        def dfs(r, c):
            area = 0
            nonlocal max_area
            if r < 0 or c < 0 or r >= ROW or c >= COL or grid[r][c] == 0 or (r,c) in seen:
                return 0
            seen.add((r,c))
            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and (r, c) not in seen:
                    area = dfs(r,c)
                    max_area = max(max_area, area)
        return max_area
                    
                


        