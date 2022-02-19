from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        tmp = 0
        tmpi = 0
        tmpv = height[0]
        for i, v in enumerate(height):
            if v >= tmpv:
                ans += tmp
                tmpi = i
                tmpv = v
                tmp = 0
            else:
                tmp += (tmpv - v)

        height.reverse()
        tmp = 0
        tmpi = len(height)
        tmpv = height[0]
        for i, v in enumerate(height):
            if v > tmpv:
                ans += tmp
                tmpi = i
                tmpv = v
                tmp = 0
            else:
                tmp += (tmpv - v)

        return ans


if __name__ == '__main__':
    a = Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print(a)
