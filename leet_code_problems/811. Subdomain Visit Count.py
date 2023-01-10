class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count=defaultdict(int)
        for i in cpdomains:
            sep=i.split()
            val=int(sep[0])
            dom=list(sep[1].split("."))
            for j in range(len(dom)):
                count[".".join(dom[j:])]+=val
        result=[]
        for domains,counts in count.items():
            result.append(f"{counts} {domains}")
        return result

            
