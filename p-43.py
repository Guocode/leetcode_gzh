class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # return str(int(num1)*int(num2))
        len1 = len(num1)
        len2 = len(num2)
        i1 = 0
        i2 = 0
        ans = ""
        step = 0
        for i in range(min(len1,len2)):
            multp = int(num1[len1-1-i])*int(num2[len2-1-i])+step
            ans+=str(multp%10)
            step = multp//10

        return ans
if __name__ == '__main__':
    a = Solution().multiply("123","456")
    print(a)