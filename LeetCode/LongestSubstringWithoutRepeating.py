class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dic = {}
        head = 0
        length = 0
        for i in xrange(len(s)):
            cur = i
            if s[cur] in dic and head <= dic[s[cur]]:
                head = dic[s[cur]] + 1
            else:
                newLen = cur - head + 1
                length = max(length, newLen)
            dic[s[cur]] = cur
        return length