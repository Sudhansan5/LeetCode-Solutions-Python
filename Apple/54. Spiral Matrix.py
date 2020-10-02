from typing import List


class Solution:
    def spiralOrder(self, A: List[List[int]]) -> List[int]:
        if not A:
            return []
        m = len(A)
        n = len(A[0])
        ans = []
        T = 0
        B = m - 1
        L = 0
        R = n - 1
        directions = 0
        while T <= B and L <= R:
            if directions == 0:
                for i in range(L, R + 1):
                    ans.append(A[T][i])
                T += 1
                directions = 1
            elif directions == 1:
                for i in range(T, B + 1):
                    ans.append(A[i][R])
                R -= 1
                directions = 2
            elif directions == 2:
                for i in range(R, L - 1, -1):
                    ans.append(A[B][i])
                B -= 1
                directions = 3
            else:
                for i in range(B, T - 1, -1):
                    ans.append(A[i][L])
                L += 1
                directions = 0
        return ans
