class TrieNode:
    def __init__(self) -> None:
        self.is_end = False
        self.children = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        current = self.root
        for i in word:
            if i not in current.children:
                current.children[i] = TrieNode()
            current = current.children[i]
        current.is_end = True

    def search(self, word: str) -> bool:
        def dfs(j,root):
            current = root
            for i in range(j,len(word)):
                if word[i]==".":
                    for val in current.children.values():
                        if dfs(i+1,val):
                            return True
                    return False
                elif word[i] not in current.children:
                    return False
                current = current.children[word[i]]
            return current.is_end
        return dfs(0,self.root)
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
