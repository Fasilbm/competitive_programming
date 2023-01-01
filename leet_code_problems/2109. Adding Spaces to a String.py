class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        output=[]
        i=0
        j=0
        spaces.append(-1)
        while j<len(s):
            space_ptr=spaces[i]
            if j!=space_ptr:
                output.append(s[j])
                j+=1
            else:
                output.append(" ")
                output.append(s[j])
                i+=1
                j+=1

        return "".join(output)
            
