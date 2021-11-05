class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        head = 0
        tail = 0
        maxlen = 0
        # occ = set()
        while tail<len(s):
            cur = s[head:tail]
            if s[tail] in cur:
                head = head+cur.index(s[tail])+1
            tail+=1

            maxlen = max(maxlen,tail-head)
        return maxlen

if __name__ == '__main__':
    a = Solution.lengthOfLongestSubstring(None,"abcabcbb")
    print(a)