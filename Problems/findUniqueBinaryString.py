class Solution:
	def findDifferentBinaryString(self, nums: List[str]) -> str:
		n = len(nums[0])
		num_ones = [2**(n-1) for _ in range(n)]
		num_zeros = [2**(n-1) for _ in range(n)]
		for i in range(len(nums)):
			for j in range(len(nums[i])):
				if nums[i][j] == '0':
					num_zeros -= 1
				if nums[i][j] == "1":
					num_ones[i][j] -=1
		res = ["0" for _ in range(n)]
		for i in range(n):
			if num_zeros[i] > 0:
				continue
			elif num_ones[i] > 0:
				res[i] = "1"
		return "".join(res)