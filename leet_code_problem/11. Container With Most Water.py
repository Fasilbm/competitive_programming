class Solution:
    def maxArea(self, height: List[int]) -> int:
        # intitalize my pointers
        l=0
        r=len(height)-1
        # Return variable
        res=0
        curr_area=0
        # iteration
        while l!=r:
            # compare the two indices value
            if height[l]>=height[r]:
                curr_area=height[r]*(r-l)
                r-=1
            else:
                curr_area=height[l]*(r-l)
                l+=1

            res=max(res,curr_area)
        return res
          # Time Complexity O(n)
          # Pace complexity O(1)
                
            
            
            
        
        
        
        
