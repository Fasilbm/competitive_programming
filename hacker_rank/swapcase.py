def swap_case(s):
    swapped=""
    for i in s:
        if i.islower():
            swapped+=i.upper()
        elif i.isupper():
            swapped+=i.lower()
        else:
            swapped+=i
    return swapped

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
