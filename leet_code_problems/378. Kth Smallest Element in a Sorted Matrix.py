class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        arr=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                arr.append(-1*matrix[i][j])
        heapq.heapify(arr)
        for i in range(len(arr)-k):
            heapq.heappop(arr)
        
        return (-1*(heapq.heappop(arr)))
