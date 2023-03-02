class Solution:
    def minWindow(self, s: str, t: str) -> str:

        tcount=Counter(t)
        scount={}
        
        max_len=10**6
        p1=10**6
        p2=0
        l=0
        s_list=list(s)
        have=len(tcount)
        need=0
        for r in range(len(s_list)):

            if s_list[r] in t:
                scount[s_list[r]]=1+scount.get(s_list[r],0)

            if s_list[r] in scount and scount[s_list[r]] == tcount[s_list[r]]:                 
                    need+=1

            while need==have:

                if r-l+1 < max_len and p1-p2+1>r-l+1:

                    p1=r
                    p2=l                
                    
                if s_list[l] in scount:
                        
                    scount[s_list[l]]=-1+scount.get(s_list[l],0)

                    if scount[s_list[l]]<tcount[s_list[l]]:
                            need-=1
                l+=1

        if p1-p2==max_len:

            return ""

        else:

            return "".join(s_list[p2:p1+1])


            

            

            

            




        
