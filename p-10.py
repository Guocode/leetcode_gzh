class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        shead = 0
        star = False
        curs = ""
        for pid,_p in enumerate(p):
            if ord(_p)<=ord('z') and ord(_p)>=ord('a'):
                if s[shead]!=_p:
                    return False
                else:
                    curs = _p
                    shead+=1
                    continue
            if _p=='*':
                if 
                _p[pid-1]

            if _p=='.':
                pass

        return

if __name__ == '__main__':

    Solution().isMatch("aa","a*")