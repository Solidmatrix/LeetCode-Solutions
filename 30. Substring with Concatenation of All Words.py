class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result = []
        keywords = {}
        if len(words) == 0:
            return result
        length = len(words[0])
        size = length * len(words)
        for k in words:
            if k in keywords:
                keywords[k] += 1
            else:
                keywords[k] = 1
        for i in xrange(length):
            pos = i - length
            while pos + size < len(s):
                key = {}
                pos += length
                ss = s[pos: pos+length]
                minpos = -1
                while ss in keywords:
                    if minpos == -1:
                        minpos = pos
                    if ss not in key:
                        key[ss] = []
                    while len(key[ss]) and key[ss][0] < minpos:
                        key[ss].pop(0)
                    if len(key[ss]) == keywords[ss]:
                        minpos = key[ss].pop(0) + length
                    key[ss].append(pos)
                    if pos - minpos + length == size:
                        result.append(minpos)
                    pos += length
                    ss = s[pos: pos+length]
        return result

        