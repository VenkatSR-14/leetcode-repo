class Solution:
	def addBinary(self, a:str, b:str) -> str:
		if len(a) < len(b):
			b, a = a, b
		carry, i = 0, 0
		a, b = a[::-1], b[::-1]
		res = ""
		while i < len(a):
			sum_val = int(a[i]) + (int(b[i] if i < len(b) else 0)) + carry
			if sum_val > 1:
				carry = 1
				res = res + (sum_val % 2)
			else:
				carry = 0
				res = res + str(sum_val)
			i += 1
		res = res + str(carry)
		return str(int(res[::-1]))


soln = Solution()
print(soln.addBinary("11", "1"))
