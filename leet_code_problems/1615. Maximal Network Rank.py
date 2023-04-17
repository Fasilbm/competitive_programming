class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        adj_list={}
        for i in range(n):
            adj_list[i]=[]
        for i,j in roads:
            adj_list[i].append(j)
            adj_list[j].append(i)
        keys=[]
        for key in adj_list.keys():
            keys.append(key)
        ans=[]
        for i in range(len(keys)):
            for j in range(i+1,len(keys)):
                if keys[i] in adj_list[keys[j]]:
                    count=len(adj_list[keys[i]])+len(adj_list[keys[j]])-1
                    ans.append(count)
                else:
                    count=len(adj_list[keys[i]])+len(adj_list[keys[j]])
                    ans.append(count)
        return max(ans)


        
