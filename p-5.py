from math import floor, ceil


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ls = len(s)
        begin = 0
        maxlen = 1
        if ls<2:
            return s
        ds = [[False]*ls for _ in range(ls)]
        for i in range(ls):
            ds[i][i]=True
        for L in range(2,ls+1):
            for i in range(ls):
                j = i+L-1
                if j>ls-1:
                    break
                if L<3:
                    ds[i][j] = s[i]==s[j]
                else:
                    ds[i][j] = (ds[i+1][j-1] and s[i]==s[j])
                if ds[i][j] and L>maxlen:
                    begin=i
                    maxlen=L
        return s[begin:begin+maxlen]
if __name__ == '__main__':
    a  = Solution().longestPalindrome("ab")
    print(a)