class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        n = len(vals)
        graph = [[] for _ in range(n)]
        for u, v in edges: 
            graph[u].append(v)
            graph[v].append(u)
        ans = -inf 
        for i, u in enumerate(graph): 
            u.sort(key=vals.__getitem__, reverse=True)
            cand = vals[i] + sum(max(0, vals[x]) for x in u[:k])
            ans = max(ans, cand)
        return ans 