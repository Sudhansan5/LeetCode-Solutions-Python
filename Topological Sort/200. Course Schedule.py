from collections import defaultdict,deque
class Solution:
    def canFinish(self, A, B):
        graph = defaultdict(list)
        inDegree = {}
        q = deque()

        for i in range(A):
            inDegree[i] = 0

        for i, j in B:
            graph[i].append(j)

        for i in graph:
            for j in graph[i]:
                if j not in inDegree:
                    inDegree[j] = 1
                else:
                    inDegree[j] += 1

        for i in inDegree:
            if inDegree[i] == 0:
                q.append(i)
        ans = []
        while q:
            i = q.popleft()
            ans.append(i)

            for j in graph[i]:
                inDegree[j] -= 1
                if inDegree[j] == 0:
                    q.append(j)

        return 1 if len(ans) == A else 0
