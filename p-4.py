import bisect
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)

        if l1 == 0:
            if l2 % 2 == 0:
                return (nums2[l2 // 2 - 1] + nums2[l2 // 2]) / 2
            else:
                return nums2[l2 // 2]
        if l2 == 0:
            if l1 % 2 == 0:
                return (nums1[l1 // 2 - 1] + nums1[l1 // 2]) / 2
            else:
                return nums1[l1 // 2]
        if nums1[0] > nums2[l2 - 1]:
            if (l1 + l2) % 2 == 0:
                return ((nums2 + nums1)[(l1 + l2) // 2 - 1] + (nums2 + nums1)[(l1 + l2) // 2]) / 2
            else:
                return (nums2 + nums1)[(l1 + l2) // 2]
        if nums1[l1 - 1] < nums2[0]:
            if (l1 + l2) % 2 == 0:
                return ((nums1 + nums2)[(l1 + l2) // 2 - 1] + (nums1 + nums2)[(l1 + l2) // 2]) / 2
            else:
                return (nums1 + nums2)[(l1 + l2) // 2]
        #少的往多的里找
        if l1>l2:
            lo = 0
            hi = l1
            for num2 in nums2:#还可以提前终止
                inind = bisect.bisect_left(nums1,num2,lo)
                lo=inind
                nums1.insert(inind,num2)
            if (l1 + l2) % 2 == 0:
                return (nums1[(l1 + l2) // 2 - 1] + nums1[(l1 + l2) // 2]) / 2
            else:
                return nums1[(l1 + l2) // 2]

        else:
            lo = 0
            hi = l2
            for num1 in nums1:#还可以提前终止
                inind = bisect.bisect_left(nums2,num1,lo)
                lo=inind
                nums2.insert(inind,num1)
            if (l1 + l2) % 2 == 0:
                return (nums2[(l1 + l2) // 2 - 1] + nums2[(l1 + l2) // 2]) / 2
            else:
                return nums2[(l1 + l2) // 2]

if __name__ == '__main__':
    a = Solution().findMedianSortedArrays([1, 2], [1,1])
    print(a)
