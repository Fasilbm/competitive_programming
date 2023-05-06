#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        maximum=i
        while True:
            left=2*i+1
            right=2*i+2
            if left<=n and arr[left]>arr[maximum]:
                maximum=left
            if right<=n and arr[maximum]<arr[right]:
                maximum=right
            if maximum != i:
                arr[i],arr[maximum]=arr[maximum],arr[i]
                self.heapify(arr,n,maximum)
                return
            else:
                return
            
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(len(arr)//2 - 1, -1 , -1):
            self.heapify(arr,n,i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        n=len(arr)-1
        self.buildHeap(arr,n)
        while n>=1:
            arr[0],arr[n]=arr[n],arr[0]
            self.heapify(arr,n-1,0)
            n-=1
      
            
        
    
            

