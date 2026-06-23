class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        
        dp_down = [1] * m
        dp_up = [1] * m
        
        for _ in range(2, n + 1):
            new_dp_down = [0] * m
            new_dp_up = [0] * m
            
            s = 0
            for i in range(m):
                new_dp_down[i] = s
                s = (s + dp_up[i]) % MOD
            
            s = 0
            for i in range(m - 1, -1, -1):
                new_dp_up[i] = s
                s = (s + dp_down[i]) % MOD
                
            dp_down = new_dp_down
            dp_up = new_dp_up
            
        return (sum(dp_down) + sum(dp_up)) % MOD