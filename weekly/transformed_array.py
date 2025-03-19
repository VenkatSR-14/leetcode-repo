from typing import List
def constructTransformedArray(self, nums: List[int]) -> List[int]:
    res = [0] * len(nums)
    for i, num in enumerate(nums):
        if num < 0:
            index = (i - num) % len(nums)
            res[i] = nums[index]
        elif num == 0:
            res[i] = num
        else:
            index = (i + nums[i]) % len(nums)
            res[i] = nums[index]
    return res