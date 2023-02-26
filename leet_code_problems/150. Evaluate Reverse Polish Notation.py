class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        ans=int(tokens[0])
        for i in tokens:
            if i!="+" and i!="-" and i!="*" and i!="/":
                stack.append(int(i))
            else:
                if i=="+":
                    ans=stack[-2]+stack[-1]
                elif i=="-":
                    ans=stack[-2]-stack[-1]
                elif i=="*":
                    ans=stack[-2]*stack[-1]
                else:
                    ans=int(stack[-2]/stack[-1])
                
                stack.pop()
                stack.pop()
                stack.append(ans)
        return ans
     
