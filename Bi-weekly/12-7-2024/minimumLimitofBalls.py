"""
You are given an integer array nums where the ith bag contains nums[i] balls. You are also given an integer maxOperations.

You can perform the following operation at most maxOperations times:

Take any bag of balls and divide it into two new bags with a positive number of balls.
For example, a bag of 5 balls can become two new bags of 1 and 4 balls, or two new bags of 2 and 3 balls.
Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.

Return the minimum possible penalty after performing the operations.
"""

from typing import List
import math

class Solution:
    def minimumSize(self, nums:List[int], maxOperations:int) -> int:
        def is_possible(num):
            total_operations = 0
            for i in range(len(nums)):
                total_operations += (nums[i] - 1)//num
            return total_operations <= maxOperations
    
        left = 0
        right = max(nums)
        
        while left < right:
            mid = (left + right)//2
            if is_possible(mid):
                right = mid
            else:
                left = mid + 1
        return left

            