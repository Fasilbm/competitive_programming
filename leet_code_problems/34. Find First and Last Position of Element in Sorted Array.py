class Solution:
   def searchRange(self, nums: List[int], target: int) -> List[int]:

        ans = []

        l = 0

        r = len(nums) - 1

        while l <= r:

            mid = l + (r - l) // 2

            if nums[mid] > target :

                r = mid - 1

            elif nums[mid] < target :

                l = mid + 1

            else:

                l = 0

                r = mid

                while l <= r :
                   
                   mid1 = l + (r - l) // 2

                   if nums[mid1] == target :

                       r = mid1 - 1

                   else:

                       l = mid1 + 1

                ans.append(l)

                l = mid

                r = len(nums) - 1

                while l <= r :
                    
                    mid2 = l + (r - l) // 2

                    if nums[mid2] == target :

                        l = mid2 + 1

                    else:

                        r = mid2 - 1


                ans.append(r)

                return ans

        return [-1,-1]



