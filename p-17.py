from typing import List

map = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ret = []
        def bt(di, si, cc):
            if si == len(di):
                return
            for c in map[di[si]]:
                if si == len(di) - 1:
                    ret.append(cc + c)
                else:
                    bt(di, si + 1, cc + c)

        bt(digits, 0, "")
        return ret


if __name__ == '__main__':
    a = Solution().letterCombinations("2")
    print(a)
