class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        numsRows = rowIndex + 1

        def helper(numsRows):

            if numsRows == 1 :

                return [[1]]

            curr = helper(numsRows-1)

            lastrow = curr[-1]
            
            newrow = [ ]

            for i in range(len(lastrow)-1):

                newrow.append(lastrow[i]+lastrow[i+1])

            updated = [1] + newrow + [1]

            return curr + [updated]

        ans = helper(numsRows)

        return ans[rowIndex]



   




        



                    
                
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        numsRows = rowIndex + 1

        def helper(numsRows):

            if numsRows == 1 :

                return [[1]]

            curr = helper(numsRows-1)

            lastrow = curr[-1]
            
            newrow = [ ]

            for i in range(len(lastrow)-1):

                newrow.append(lastrow[i]+lastrow[i+1])

            updated = [1] + newrow + [1]

            return curr + [updated]

        ans = helper(numsRows)

        return ans[rowIndex]



   




        



                    
                
