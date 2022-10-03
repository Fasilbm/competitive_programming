import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        notations = {'+':operator.add,
                     '-':operator.sub,'*':operator.mul,'/':operator.truediv}
        for i in tokens:
            if i=='+'or i=='-' or i=='*' or i=='/':
                second=stack.pop()
                first=stack.pop()
                stack.append(int(notations[i](first,second)))
            else:
                stack.append(int(i))
        return stack[-1]
    # Time complexity O(n)
    # Space Complexity O(1)
        
