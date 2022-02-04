#https://leetcode.com/problems/add-binary/
def add_binary(a,b):
    reverse_a=a[::-1]
    reverse_b=b[::-1]
    lenA=len(a)
    lenB=len(b)
    if lenA>lenB:
        maxLen=lenA
        reverse_b+="0"* (lenA-lenB)
    else:
        maxLen=lenB
        reverse_a+="0"* (lenB-lenA)
    carry=0
    output=[]
    for i in range(maxLen):
        if reverse_a[i]=='0' and reverse_b[i]=='0':
            result= 0+ carry
            carry=0
        elif reverse_a[i]=='1' and reverse_b[i]=='1':
            result = 0 + carry
            carry=1
        else:
            if carry==0:
                result=1
            else:
                result=0
                carry=1
        output.append(result)
    if carry:
        output.append(carry)
    return " ".join(str(x) for x in output[::-1])
print(add_binary('11','1'))
        