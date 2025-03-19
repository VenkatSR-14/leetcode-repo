from functools import lru_cache
from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        target_subset_sum = total_sum // k
        nums.sort(reverse=True)  # Sort to optimize by trying larger numbers first
        n = len(nums)
        
        @lru_cache(None)
        def recurse(index, subset_sums):
            if index == n:
                return all(s == target_subset_sum for s in subset_sums)
            
            num = nums[index]
            for i in range(k):
                if subset_sums[i] + num > target_subset_sum:
                    continue
                # Try placing the number in subset i
                new_subset_sums = list(subset_sums)
                new_subset_sums[i] += num
                if recurse(index + 1, tuple(new_subset_sums)):
                    return True
                # Backtrack (implicit due to new_subset_sums being local)
                
                # Optimization: If the current subset is empty, no need to try further
                if subset_sums[i] == 0:
                    break
            
            return False

        # Start recursion with all subsets empty
        return recurse(0, tuple([0] * k))