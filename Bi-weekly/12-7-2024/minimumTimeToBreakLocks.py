import math
from typing import List
class Solution:
    def findMinimumTimeToBreakLocks(self, strength: List[int], K:int) -> int:
        n = len(strength)
        dp = [float('inf')] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            count = bin(mask).count(1)
            factor = 1 + count * K
            for i in range(n):
                if not (mask & 1 << i):
                    required_strength = strength[i]
                    total_time_needed = math.ceil(required_strength/factor)
                    new_mask = mask | (1 << i)
                    dp[new_mask] = min(dp[new_mask], dp[mask] + total_time_needed)
        return dp[(1 <<n) -1 ]         