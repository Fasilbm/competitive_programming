class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        target = max(arr)

        l = 0
        r = len(arr) - 1

        while l <= r :

            mid = l + (r - l) // 2

            if arr[mid] == target :

                return mid

            elif arr[mid] < target :

                if arr[mid-1] < arr[mid+1] :

                    l = mid

                else:

                    r = mid



