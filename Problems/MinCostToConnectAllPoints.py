class UnionFind:
	def __init__(self, n):
		self.rank = [1 for _ in range(n)]
		self.root = [i for i in range(n)]
		self.n = n

	def find(self, x):
		if self.root[x] != x:
			self.root[x] = self.find(self.root[x])
		return self.root[x]

	def Union(self, x, y):
		rootX = self.find(x)
		rootY = self.find(y)
		if rootX != rootY:
			if self.rank[rootX] > self.rank[rootY]:
				self.root[rootY] = rootX
			elif self.rank[rootY] > self.rank[rootX]:
				self.root[rootX] = rootY
			else:
				self.root[rootY] = rootX
				self.rank[rootX] += 1


class Solution:
	def minCostConnectPoints(self, points: List[List[int]]) -> int:
		graph = []
		num_edges = 0
		n = len(points)
		for i in range(len(points)):
			for j in range(len(points)):
				if i != j:
					x1, y1 = points[i]
					x2, y2 = points[j]
					manhattan_distance = abs(x1 - x2) + abs(y1 - y2) 
					graph.append((i, j, manhattan_distance))
		graph.sort(key = lambda x: x[2])
		unionfind = UnionFind(n)
		total_weight = 0
		for src, dest, weight in graph:
			if unionfind.find(src) == unionfind.find(dest):
				continue
			else:
				unionfind.Union(src, dest)
				num_edges += 1
				total_weight += weight
				if num_edges == n - 1:
					break
		return total_weight