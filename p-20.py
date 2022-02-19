class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []
        for _s in s:
            if _s=='(' or _s=='[' or _s=='{':
                stack.append(_s)
            if _s==')':
                if len(stack)==0:
                    return False
                if stack.pop()!='(':
                    return False
            if _s==']':
                if len(stack)==0:
                    return False
                if stack.pop()!='[':
                    return False
            if _s=='}':
                if len(stack)==0:
                    return False
                if stack.pop()!='{':
                    return False
        if len(stack)!=0:
            return False
        return True

if __name__ == '__main__':
    a = Solution().isValid(")")
    print(a)