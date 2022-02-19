class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31-1
        ans = 0
        sign = 1
        signflag = False
        if len(s)==0:
            return ans
        breakflag = True
        while breakflag:
            if len(s)>0:
                if s[0]==" ":
                    s = s[1:]
                else:
                    breakflag = False
            else:
                breakflag=False
        for _s in s:
            if not signflag:
                if _s=="-":
                    sign = -1
                    signflag = True
                    continue
                if _s=="+":
                    signflag = True
                    sign = 1
                    continue
            if ord(_s)>=ord("0") and ord(_s)<=ord("9"):
                signflag=True
                ans=int(_s)+ans*10
                if ans*sign>INT_MAX:
                    return INT_MAX
                if ans*sign<INT_MIN:
                    return INT_MIN
            else:
                break
        return ans*sign

if __name__ == '__main__':
    a  =  Solution().myAtoi("   +0 123")
    print(a)