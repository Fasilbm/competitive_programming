class Solution:
    def isValidSudoku(self, board):

        count=set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]!="." and board[i][j] not in count:
                    count.add(board[i][j])
                elif board[i][j]!="." and board[i][j] in count:
                    return False
            count=set()
        count=set()
        for i in range(len(board[0])):
            for j in range(len(board)):
                if board[j][i]!="." and board[j][i] not in count:
                    count.add(board[j][i])
                elif board[j][i]!="." and board[j][i] in count:
                    return False
            count=set()

        n=9
        start_r,row=0,3
        start_c,col=0,3
        while row<=n:
            count=set()
            while col<=n:
                for i in range(start_r,row):
                    for j in range(start_c,col):
                        if board[i][j]!="." and board[i][j] not in count:
                            count.add(board[i][j])
                        elif board[i][j]!="." and board[i][j] in count:
                            return False
                count=set()
                start_c+=3
                col+=3
            start_c=0
            col=3
            start_r+=3
            row+=3
        return True
