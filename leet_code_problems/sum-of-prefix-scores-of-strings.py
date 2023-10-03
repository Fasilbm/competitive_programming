class TrieNode:
    def __init__(self) -> None:
        self.is_end = False
        self.children = {}
        self.val=0

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str):
        current = self.root
       
        for i in word:
            if i not in current.children:
                current.children[i] = TrieNode()
            current = current.children[i]
            current.val+=1
        current.is_end = True
    def search(self,word):
        current = self.root
        count=0
        for i in word:
            current = current.children[i]
            count+=current.val
        return count

        
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()

        for i in words:
            trie.insert(i)

        return [trie.search(word) for word in words]
        
        
