class Solution: 
    def select(self, arr, i):
        # code here
        start=arr[i]
        
    def selectionSort(self, arr,n):
        for i in range(len(arr)-1):
            minmum=i
            for j in range(i+1,len(arr)):
                 if arr[j]<arr[minmum]:
                       minmum=j
            arr[i],arr[minmum]=arr[minmum],arr[i]
        return arr
