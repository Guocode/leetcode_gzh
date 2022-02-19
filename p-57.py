from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        ans = []
        for i,inter in enumerate(intervals):
            if inter[0]>newInterval[0]:
                break
            ans.append(inter)

        if i>0 and intervals[i-1][1]>=newInterval[0]:#merge intervals[i-1] and newInterval
            left = intervals[i-1]
            newInterval = [left[0],max(left[1],newInterval[1])]

        for j in range(i,len(intervals)):
            if intervals[j][0]<=newInterval[1]:
                newInterval[1] = intervals[j][1]
            else:
                break
        ans.append(newInterval)
        for k in range(j,len(intervals)):
            ans.append(intervals[k])

        return ans

if __name__ == '__main__':
    a  =Solution().insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8])
    print(a)