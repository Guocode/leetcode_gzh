from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # if len(height)==2:
        #     return min(height)
        # return max(min(height[0],height[-1])*(len(height)-1),self.maxArea(height[1:]),self.maxArea(height[:-1]))
        head = 0
        tail = len(height)-1
        ans = 0
        while tail>head:
            maxA = min(height[head], height[tail]) * (tail - head)
            ans = max(ans,maxA)
            if height[head]< height[tail]:
                head+=1
            else:
                tail-=1
        return ans

if __name__ == '__main__':
    a  = Solution().maxArea([1,8,6,2,5,4,8,3,7])
    print(a)