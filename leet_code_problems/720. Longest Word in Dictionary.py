class TrieNode:
    def __init__(self) -> None:
        self.is_end = False
        self.children = {}
        self.val=""

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str):
        current = self.root
       
        for i in word:
            if i not in current.children:
                current.children[i] = TrieNode()
            current = current.children[i]
        current.is_end = True
        current.val = word

    def search(self,word):
        current = self.root
        queue = deque([current])
        ref=""
        while queue:
            candidate= queue.popleft()
            for node in candidate.children.values():
                if node.is_end:
                    queue.append(node)
                    if len(node.val)>len(ref):
                        ref=node.val
        return ref

class Solution:
    def longestWord(self, words: List[str]) -> str:

        trie = Trie()
        words.sort()
        for i in words:
            trie.insert(i)
        return trie.search(1)
