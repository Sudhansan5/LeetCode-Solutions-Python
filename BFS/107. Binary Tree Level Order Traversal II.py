from collections import deque


class Solution:
    def levelOrderBottom(self, root):
        if not root: return []
        q = deque()
        q.append(root)
        ans = []
        while q:
            size = len(q)
            tmp = []
            for _ in range(size):
                curr = q.popleft()
                tmp.append(curr.val)

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)
            ans.append(tmp)
        return ans[::-1]
