# good solution
class Solution(object):
    
    def similar(self, s1, s2):
        d1 = {}
        d2 = {}
        for s in s1:
            if s in d1:
                d1[s] += 1
            else:
                d1[s] = 0
        for s in s2:
            if s in d2:
                d2[s] += 1
            else:
                d2[s] = 0
                
        if d1 == d2:
            return True
        return False
    
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            print("error")
            return False
        
        if len(s1) == 0:
            return True
        
        if s1[0] == s2[0] and self.isScramble(s1[1: ], s2[1: ]):
            return True
        if s1[0] == s2[-1] and self.isScramble(s1[1: ], s2[: -1]):
            return True
        if s1[-1] == s2[0] and self.isScramble(s1[: -1], s2[1: ]):
            return True
        if s1[-1] == s2[-1] and self.isScramble(s1[: -1], s2[: -1]):
            return True
        
        for i in range(2, 1 + len(s1)/2):
            if self.similar(s1[: i], s2[: i]) and self.isScramble(s1[: i], s2[: i]) and self.isScramble(s1[i: ], s2[i: ]):
                return True
            if self.similar(s1[: i], s2[-i: ]) and self.isScramble(s1[: i], s2[-i: ]) and self.isScramble(s1[i: ], s2[: -i]):
                return True
            if self.similar(s1[-i: ], s2[: i]) and self.isScramble(s1[-i: ], s2[: i]) and self.isScramble(s1[: -i], s2[i: ]):
                return True
            if self.similar(s1[-i: ], s2[-i: ]) and self.isScramble(s1[-i: ], s2[-i: ]) and self.isScramble(s1[: -i], s2[: -i]):
                return True
        return False




# bad solution
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            print("error")
            return False
        
        if len(s1) == 1:
            if s1 == s2:
                return True
            if s1 != s2:
                return False
        
        for i in range(1, len(s1)/2 + 1):
            if self.isScramble(s1[: i], s2[: i]) and self.isScramble(s1[i: ], s2[i: ]):
                return True
            if self.isScramble(s1[: i], s2[-i: ]) and self.isScramble(s1[i: ], s2[: -i]):
                return True
            if self.isScramble(s1[-i: ], s2[: i]) and self.isScramble(s1[: -i], s2[i: ]):
                return True
            if self.isScramble(s1[-i: ], s2[-i: ]) and self.isScramble(s1[: -i], s2[: -i]):
                return True
        return False