class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer=[0]*len(temperatures)
        stack=[] 
        x=len(temperatures)-1
        for i in range(len(temperatures)):
           
                while stack and temperatures[x]>=temperatures[stack[-1]]:
                    stack.pop()
            
                if stack and temperatures[x]<temperatures[stack[-1]]: 
                    answer[x]=stack[-1]-x
        
                stack.append(x)
                x-=1
        return answer
#Timecomplexity O(n**2)
#space complexity O(n)
