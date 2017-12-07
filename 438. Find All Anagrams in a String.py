class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        ordA = ord('a')
        product1 = product2 = 1
        ll = len(p)
        result = []
        for i in xrange(ll):
            product1 *= prime[ord(p[i])-ordA]
            product2 *= prime[ord(s[i])-ordA]
        for i in xrange(len(s)-ll+1):
            if product1 == product2:
                result.append(i)
            if i+ll < len(s):
                if s[i] == s[i+ll]:
                    continue
                else:
                    product2 = product2 / prime[ord(s[i])-ordA] * prime[ord(s[i+ll])-ordA]
        return result