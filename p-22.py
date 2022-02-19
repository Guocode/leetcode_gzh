from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        a = ""
        ans = []
        an = n
        bn = n
        def bt(a,b,c):
            if b==0 and c==0:
                ans.append(a)
                return
            if b>0:
                bt(a+"(",b-1,c)
            if c>b and c>0:
                bt(a+")",b,c-1)
                    
        bt(a,an,bn)

        return ans
if __name__ == '__main__':

    x = Solution().generateParenthesis(3)
    print(x)
