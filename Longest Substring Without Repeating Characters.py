class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c, t = 0, ''
        for i in s:
            if i in t:

                c = len(t) if len(t) > c else c
                t = t[t.index(i) + 1:]
            t += i
        return len(t) if len(t) > c else c