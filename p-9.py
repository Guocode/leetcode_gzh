from math import floor, ceil


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        a = str(x)
        if a[:floor(len(a)/2)]==a[ceil(len(a)/2):][::-1]:
            return True
        else:
            return False


if __name__ == '__main__':
    a = Solution().isPalindrome(1221)
    print(a)