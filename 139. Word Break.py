class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        length = len(s)
        cut = [False] * (length + 1)
        cut[0] = True;
        lenDict = {}
        for w in wordDict:
            lenDict[len(w)] = 1
        lenDict = lenDict.keys()
        for i in xrange(1, length+1):
            for j in lenDict:
                if cut[i-j] and s[i-j: i] in wordDict:
                    cut[i] = True
                    break
        return cut[length]