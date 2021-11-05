from typing import List


class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for nid, n in enumerate(nums):
    #         if target-n in nums:
    #             if nums.index(target-n)==nid:
    #                 continue
    #             return [nid,nums.index(target-n)]
    #     return [] #500ms

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for nid, n in enumerate(nums):
            if target - n in hashtable:
                return [nid, hashtable[target - n]]
            hashtable[n] = nid
        return []  # 30ms

# 第一种解法每次需要去所有list里面查找，而第二种解法不需要查找

if __name__ == '__main__':
    ret = Solution().twoSum([3, 2, 4], 6)
    print(ret)
