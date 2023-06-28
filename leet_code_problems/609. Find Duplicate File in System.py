class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
 
        dup = defaultdict(list)
        for i in paths:
            curr_path = i.split()
            root = curr_path[0]
            for j in range(1,len(curr_path)):
                curr_file = curr_path[j].split("(")
                curr_file_name = curr_file[0]
                curr_file_content = curr_file[1]
                dup[curr_file_content].append( root + "/" +curr_file_name)
        ans = []
        for cont in dup.keys():
            if len(dup[cont]) > 1:
                ans.append(dup[cont])
        return (ans)
