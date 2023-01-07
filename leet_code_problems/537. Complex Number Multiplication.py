class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        sp1=num1.split("+")
        sp2=num2.split("+")
        a=int(sp1[0])
        b=int(sp1[1][:-1])
        c=int(sp2[0])
        d=int(sp2[1][:-1])
        real=(a*c-b*d)
        imag=(a*d+b*c)
        return str(real)+"+"+str(imag)+"i"
        
