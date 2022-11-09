class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired=[[i,j] for i,j in sorted(zip(position,speed))]
        stack=[]
        for p,s in (paired)[::-1]:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)
