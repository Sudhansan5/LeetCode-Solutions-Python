class Solution:
    def isValid(self, A, row, col):
        if row < 0 or row >= len(A) or col < 0 or col >= len(A[0]):
            return False
        return True

    def dfs(self, A, row, col, vis):
        vis[row][col] = True

        Row = [0, 1, 0, -1]
        Col = [1, 0, -1, 0]

        for r, c in zip(Row, Col):
            new_r = row + r
            new_c = col + c

            if self.isValid(A, new_r, new_c) and not vis[new_r][new_c] and A[new_r][new_c] == 'O':
                vis[new_r][new_c] = True
                self.dfs(A, new_r, new_c, vis)

    def solve(self, A):
        if not A: return []
        m = len(A)
        n = len(A[0])
        vis = [[False] * n for _ in range(m)]

        for i in range(m):
            if A[i][0] == 'O':
                self.dfs(A, i, 0, vis)

            if A[i][n - 1] == 'O':
                self.dfs(A, i, n - 1, vis)

        for j in range(n):
            if A[0][j] == 'O':
                self.dfs(A, 0, j, vis)

            if A[m - 1][j] == 'O':
                self.dfs(A, m - 1, j, vis)

        for i in range(m):
            for j in range(n):
                if not vis[i][j] and A[i][j] == 'O':
                    A[i][j] = 'X'
