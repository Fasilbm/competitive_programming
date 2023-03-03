class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired=[[i,j] for i,j in sorted(zip(position,speed))]
        stack=[]
        for p,s in (paired)[::-1]:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)
    
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair=[]
        time=[]

        for i,j in enumerate(position):

            pair.append([j,speed[i]])

        pair.sort()

        for i,j in pair:

            time.append((target-i)/j)

        stack=[time[-1]]

        for i in range(len(time)-2,-1,-1):

            stack.append(time[i])

            if stack and stack[-2]>=stack[-1]:

                stack.pop()

        return len(stack)
            
