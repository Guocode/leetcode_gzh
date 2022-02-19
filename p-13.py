m = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        stack = []
        for _s in s[::-1]:
            if _s=="V" or _s=="X":
                m["I"] = -1
            if _s=="L" or _s=="C":
                m["X"] = -10
            if _s == "D" or _s == "M":
                m["C"] = -100

            ans += m[_s]
        return ans

if __name__ == '__main__':
    ret = Solution().romanToInt("MCMXCIV")
    print(ret)