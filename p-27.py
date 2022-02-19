class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a = dividend>0
        b = divisor>0
        dividend = abs(dividend)
        divisor = abs(divisor)
        ans = 0
        while True:
            dividend = dividend-divisor
            if dividend<0:
                break
            ans+=1
        if a>0:
            if b>0:
                return ans
            else:
                return -ans
        else:
            if b > 0:
                return -ans
            else:
                return ans


if __name__ == '__main__':
    a =  Solution().divide(7,-3)
    print(a)