class Solution:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        for k in range(n-1):
            tmp = ''

            i = 0
            r = 0
            while i<len(ans):
                while r<len(ans) and ans[r]==ans[i]:
                    r+=1
                tmp+=str(r-i)+ans[i]
                i=r
                r = i
            ans = tmp
        return ans

if __name__ == '__main__':
    a = Solution().countAndSay(4)
    print(a)