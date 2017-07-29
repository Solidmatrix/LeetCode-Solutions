class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        index = {}
        result = []
        ordA = ord('a')
        for string in strs:
            product = 1
            for s in string:
                product *= prime[ord(s)-ordA]
            if product in index:
                result[index[product]].append(string)
            else:
                index[product] = len(index)
                result.append([string])
        return result