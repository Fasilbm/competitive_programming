class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stack=[-1]
        length=0
        for i ,char in enumerate(s):
            if char=="(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack)!=0:
                    length=max(length,i-stack[-1])
                else:
                    stack.append(i)
        return length     
