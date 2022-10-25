class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix=[0 for i in range(n+2)]
        for i in range(len(bookings)):
            j=(bookings[i][0])
            k=(bookings[i][1])
            l=(bookings[i][2])
            prefix[j]+=l
            prefix[k+1]+=-l
        for i in range(1,len(prefix)):
            prefix[i]+=prefix[i-1]
        return (prefix[1:-1])
        
        # Time Complexity O(n)
        # Space Complexity O(n)
        
