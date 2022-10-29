class Solution:
    def countVowels(self, word: str) -> int:
        count=0
        for i,x in enumerate(word):
            if x in "aeiou":
                count+=(i+1)*(len(word)-i)
        return count
    # Time complexity O(n)
    # Space complexity O(1)
