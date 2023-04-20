class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        row = [0]*m
        col = [0]*n
        for i in range(m): 
            for j in range(n): 
                if grid[i][j]: 
                    row[i] += 1
                    col[j] += 1
        ans = [[0]*n for _ in range(m)]
        for i in range(m): 
            for j in range(n): 
                ans[i][j] = 2*row[i] + 2*col[j] - m - n
        return ans 