from collections import defaultdict
def arrayManipulation(n, queries):
    
  tracker=defaultdict(int)
  
  for i,j,k in queries:
    
    tracker[i-1]+=k
    tracker[j]-=k
    
  prefix=[j for i,j in sorted(tracker.items())]
   
  
  for i in range(1,len(prefix)):
    
    prefix[i]=prefix[i-1]+prefix[i]
    
  return max(prefix)
                
