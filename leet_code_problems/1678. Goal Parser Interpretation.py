class Solution:
    def interpret(self, command: str) -> str:

        new=[]
        count=0
        while count<len(command):
            if command[count]=="G":
                new.append("G")
                count+=1
            elif command[count]=="(" and command[count+1]==")":
                new.append("o")
                count+=2
            elif command[count]=="(" and command[count+1]=="a" and command[count+2]=="l" and command[count+3]==")":
                new.append("al")
                count+=4

        return "".join(new)
