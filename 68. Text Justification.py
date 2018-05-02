class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        length = len(words[0])
        pos = 0
        result = []
        for i in range(1, len(words)):
            if length + len(words[i]) + 1 > maxWidth:
                line = ""
                n = i - pos - 1
                if n == 0:
                    n = 1
                space = (maxWidth - length) / n
                num = maxWidth - length - space*n
                for j in range(pos, i):
                    line += words[j]
                    if j < pos + num:
                        line += " " * (space + 2)
                    elif j < i-1:
                        line += " " * (space + 1)
                line += " " * (maxWidth - len(line))
                result.append(line)
                length = len(words[i])
                pos = i
            else:
                length += len(words[i]) + 1
        line = ""
        for j in range(pos, len(words)):
            line += words[j]
            if len(line) < maxWidth:
                line += " "
        line += " " * (maxWidth - len(line))
        result.append(line)
        return result