from collections import deque
class Solution:
    def largestMerge(self, word1, word2):
        
        w1=deque(word1)
        w2=deque(word2)
        merged=""

        while w1 and w2:
            if w1>w2:
                merged+=w1[0]
                w1.popleft()
            else:
                merged+=w2[0]
                w2.popleft()
        while w1:
            merged+=w1[0]
            w1.popleft()
        while w2:
            merged+=w2[0]
            w2.popleft()

        return merged
