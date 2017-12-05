class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        maxLength = 0
        pos = 0
        for i in xrange(len(s)):
            if s[i] in dict:
                if maxLength < i - pos:
                    maxLength = i - pos
                if pos < dict[s[i]] + 1:
                    pos = dict[s[i]] + 1
            dict[s[i]] = i
        if maxLength < len(s) - pos:
            maxLength = len(s) - pos
        return maxLength