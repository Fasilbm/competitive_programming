class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids:
            while stack and i<0<stack[-1]:
                if i+stack[-1]<0:
                    stack.pop()
                    continue
                elif stack[-1]+i==0:
                    stack.pop()
                break
            else:
                stack.append(i)
        return stack
    # space complexity O(n)
    # time complexity O(n)
