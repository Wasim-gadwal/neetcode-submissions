class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [-1] * (n + 1)
        def dfs(step):
            if step <= 1:
                return 1
            if mem[step] != -1:
                return mem[step]
            mem[step] = dfs(step - 1) + dfs(step - 2)
            return mem[step]
        return dfs(n)
        