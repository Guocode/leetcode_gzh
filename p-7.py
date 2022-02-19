class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31-1
        y = 0
        sign = 1 if x>0 else -1
        x = abs(x)
        while x!=0:
            a = x % 10
            x = x // 10
            if (INT_MAX-a)//10<y or (INT_MIN-a)//10>y:
                return 0
            y = y*10+a

        return y*int(sign)

if __name__ == '__main__':
    a = Solution().reverse(-123)
    print(a)