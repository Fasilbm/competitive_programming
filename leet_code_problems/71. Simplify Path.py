class Solution:
    def simplifyPath(self, path: str) -> str:

        stack=[]
        path=list(path.split("/"))
        

        for i in range(len(path)):

            if path[i]==".." and stack:

                stack.pop()
            
            elif path[i]=="." or path[i]=="" or path[i]=="..":
                continue
            
            else:
                stack.append(path[i])


        return "/"+"/".join(stack)

       

            
