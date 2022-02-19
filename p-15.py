from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        nums.sort()
        ans = []
        a = 0
        while True:
            if a>0:
                while nums[a] == nums[a - 1]:
                    a = a + 1
            if a>=len(nums)-2:
                break
            b = a+1
            c = len(nums)-1
            while True:
                while nums[b] == nums[b + 1]:
                    b = b + 1
                while nums[c] == nums[c - 1]:
                    c = c - 1
                if nums[a]+nums[b]+nums[c]==0:
                    ans.append([nums[a],nums[b],nums[c]])
                    b = b+1
                    c = c-1
                elif nums[a]+nums[b]+nums[c]<0:
                    b = b+1
                else:
                    c = c-1
                if b>=c:
                    break
            a = a+1
        return list(ans)


if __name__ == '__main__':
    a = Solution().threeSum([0,0,0])
    print(a)