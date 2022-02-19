class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        stack = []
        stack.append(-1)
        for sid,_s in enumerate(s):
            if _s=='(':
                stack.append(sid)
            else:
                stack.pop()
                if len(stack)>0:
                    m = sid - stack[-1]
                    ans = max(m,ans)
                else:
                    stack.append(sid)
        return ans
if __name__ == '__main__':

    a = Solution().longestValidParentheses("(()()")
    print(a)