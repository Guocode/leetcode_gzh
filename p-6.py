class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        slen = len(s)
        gcout = (numRows-1)*2
        gnum = slen//gcout
        glef = slen%gcout
        news = ""
        for i in range(numRows):
            if  i==0 or i==numRows-1:
                c = 0
                j = i+c*gcout
                while j <slen:
                    news+=s[j]
                    c = c+1
                    j = i+c*gcout
            else:
                c = 0
                j = i+c*gcout
                k = (gcout-i)+c*gcout
                while j<slen or k<slen:
                    if j<slen:
                        news += s[j]
                    if k<slen:
                        news += s[k]
                    c = c+1
                    j = i + c * gcout
                    k = (gcout - i) + c * gcout
        return news

if __name__ == '__main__':
    a = Solution().convert("PAYPALISHIRING",3)
    print(a)