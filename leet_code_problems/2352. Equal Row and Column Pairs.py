class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count=0
        hash_row={}
        hash_col={}
        for i in range(len(grid)):
            hash_row[i]=grid[i]                
        for j in range(len(grid)):			
            temp=[]
            for k in range(len(grid[0])):      
                temp.append(grid[k][j])
            hash_col[j]=temp
        for l in range(len(hash_row)):
            for m in range(len(hash_col)):
                if hash_row[l]==hash_col[m]:
                    count+=1
        return count
            



            
