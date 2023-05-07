class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
    
        count=Counter(words)
        heap=[]
        for key in count.keys():
            heapq.heappush(heap,(-count[key],key))
        ans=[]
        for i in range(k):
            word,freq=heapq.heappop(heap)
            ans.append(freq)
        return ans
         
