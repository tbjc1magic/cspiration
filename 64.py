class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        w, h = len(grid[0]), len(grid)
        
        dp = [[10000]*w for _ in range(h)]
        dp[0][0] = 0
        
        for r in range(h):
            for c in range(w):
                if r>0: dp[r][c] = min(dp[r][c], dp[r-1][c])
                if c>0: dp[r][c] = min(dp[r][c], dp[r][c-1])
                dp[r][c] += grid[r][c]
                
        return dp[-1][-1]
