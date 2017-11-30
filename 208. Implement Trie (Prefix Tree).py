class node:
    def __init__(self):
        self.status = False
        # False : not end
        # True : end
        self.index = {}
        
class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        p = self.root
        for i in word:
            if i not in p.index:
                p.index[i] = node()
            p = p.index[i]
        p.status = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self.root
        for i in word:
            if i not in p.index:
                return False
            p = p.index[i]
        return p.status

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = self.root
        for i in prefix:
            if i not in p.index:
                return False
            p = p.index[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)