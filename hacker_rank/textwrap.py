import textwrap

def wrap(string, max_width):
    for i in range(len(string)):
        if i%max_width==0 and i!=0:
             print("\n",end="")
        print(string[i],end="")
    return ""

           
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
