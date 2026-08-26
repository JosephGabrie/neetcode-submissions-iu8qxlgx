class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(stairs):
            if stairs <= 0:
                return 0
            if stairs == 1:
                return 1
            if stairs == 2:
                return 2

            if stairs in memo:
                return memo[stairs]
            memo[stairs] = dfs(stairs - 2) + dfs(stairs - 1)
            return memo[stairs]
        return dfs(n)
        