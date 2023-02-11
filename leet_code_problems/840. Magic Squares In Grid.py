class Solution:
    def numMagicSquaresInside(self, grid):

        if len(grid)<3 and len(grid[0])<3:
            return 0
        start_r,row=0,3
        start_c,col=0,3
        count=0
        x=0

        def distnict():
            count=set()
            for i in range(start_r,row):
                for j in range(start_c,col):
                    if grid[i][j] in count or grid[i][j]>9 or grid[i][j]<1:
                        return False
                    else:
                        count.add(grid[i][j])
            return True

        def horizontal_sum():
            count=3
            ref=grid[start_r][start_c]+grid[start_r][start_c+1]+grid[start_r][start_c+2]
            for i in range(start_r,row):
                summ=0
                for j in range(start_c,col):
                    summ+=grid[i][j]
                if summ==ref:
                    count-=1
                else:
                    break
            if count==0:
                return True
            else:
                return False
            
        def vertical_sum():
            count=3
            ref=grid[start_r][start_c]+grid[start_r][start_c+1]+grid[start_r][start_c+2]
            for i in range(start_c,col):
                summ=0
                for j in range(start_r,row):
                    summ+=grid[j][i]
                if summ==ref:
                    count-=1
                else:
                    break
            if count==0:
                return True
            else:
                return False
            
        def fwd_dig():
            summ=0
            i=start_r
            j=start_c
            ref=grid[start_r][start_c]+grid[start_r][start_c+1]+grid[start_r][start_c+2]
            while j<col and i<row:
                summ+=grid[i][j]
                i+=1
                j+=1
            if summ==ref:
                return True
            else:
                return False
            
        def bwd_dig():
            summ=0
            i=row-1
            j=start_c
            ref=grid[start_r][start_c]+grid[start_r][start_c+1]+grid[start_r][start_c+2]
            while j<col and i>=start_r:
                summ+=grid[i][j]
                i-=1
                j+=1
            if summ==ref:
                return True
            else:
                return False

        while row<=len(grid):
            while col<=len(grid[0]):
               
                if horizontal_sum() and vertical_sum() and fwd_dig() and bwd_dig() and distnict():
                    x+=1                        
                start_c+=1
                col+=1
            start_c=0
            col=3
            start_r+=1
            row+=1

        return x

        
