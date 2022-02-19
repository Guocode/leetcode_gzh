class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        a = num%10
        b = (num//10)%10
        c = (num//100)%10
        d = (num//1000)%10
        if d>0:
            ans+="M"*d
        if c>0:
            if c<=3:
                ans+="C"*c
            elif c>3 and c<9:
                ans+= "C"*max(5-c,0)+"D"+"C"*max(c-5,0)
            else:
                ans+="CM"
        if b > 0:
            if b <= 3:
                ans += "X" * b
            elif b > 3 and b < 9:
                ans += "X" * max(5 - b, 0) + "L" + "X" * max(b - 5, 0)
            else:
                ans += "XC"
        if a > 0:
            if a <= 3:
                ans += "I" * a
            elif a > 3 and a < 9:
                ans += "I" * max(5 - a, 0) + "V" + "I" * max(a - 5, 0)
            else:
                ans += "IX"

        return ans


if __name__ == '__main__':
    ret = Solution().intToRoman(1994)
    print(ret)