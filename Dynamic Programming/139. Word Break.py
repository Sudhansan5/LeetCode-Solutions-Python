class Solution:
    def dp(self, s, dic, dp):   #Top-Down
        if s == "":
            return True

        if s in dic:
            return True

        if s in dp:
            return dp[s]

        for i in range(1,len(s)+1):
            if s[:i] in dic and self.dp(s[i:],dic,dp):
                dp[s] = True
                return dp[s]

        dp[s] = False
        return dp[s]

    def Solve(self, s, dic):
        n = len(s)
        dp = {}
        return self.dp(s, dic,dp)

    def wordBreak(self, s, dic):   #Bottom-Up
        n = len(s)
        dp = [False for _ in range(n + 1)]
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in dic:
                    dp[i] = True

        return dp[-1]


if __name__ == '__main__':
    A = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    B = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]

    s = "leetcode"
    wordDict = ["leet", "code"]

    D = "aaaaaaa"
    E = ["aaaa", "aaa"]

    C = Solution()
    print(C.Solve(A, B))
    print(C.wordBreak(A, B))
