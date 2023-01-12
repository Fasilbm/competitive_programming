class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        answer=[]
        for j in range(king[1],8):
            if [king[0],j] in queens:
                answer.append([king[0],j])
                break
        for j in range(king[1],-1,-1):
            if [king[0],j] in queens:
                answer.append([king[0],j])
                break
        for j in range(king[0],8):
            if [j,king[1]] in queens:
                answer.append([j,king[1]])
                break
        for j in range(king[0],-1,-1):
            if [j,king[1]] in queens:
                answer.append([j,king[1]])
                break
        row=king[0]
        col=king[1]
        while row>=0 and col<8:
            if [row,col] in queens:
                answer.append([row,col])
                break
            row-=1
            col+=1
        row=king[0]
        col=king[1]
        while row<8 and col>=0:
            if [row,col] in queens:
                answer.append([row,col])
                break
            row+=1
            col-=1
        row=king[0]
        col=king[1]
        while row>=0 and col>=0:
            if [row,col] in queens:
                answer.append([row,col])
                break
            row-=1
            col-=1
        row=king[0]
        col=king[1]
        while row<8 and col<8:
            if [row,col] in queens:
                answer.append([row,col])
                break
            row+=1
            col+=1

        return answer
        
        

       
        
        

            
