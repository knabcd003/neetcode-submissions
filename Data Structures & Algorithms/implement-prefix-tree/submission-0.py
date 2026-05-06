class TreeNode:
    def __init__(self):
        self.children = [None] * 26
        self.word_end = False
class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        if not word:
            return
        tmp = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not tmp.children[index]:
                tmp.children[index] = TreeNode()
            tmp = tmp.children[index]
        tmp.word_end = True
            
            

    def search(self, word: str) -> bool:
        if not word:
            return False
        tmp = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not tmp.children[index]:
                return False
            tmp = tmp.children[index]
        if not tmp.word_end:
            return False
        return True
        

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return False
        tmp = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if not tmp.children[index]:
                return False
            tmp = tmp.children[index]
        return True
        
        