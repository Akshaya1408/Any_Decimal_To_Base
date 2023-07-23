def decimal_conversion(num,base):
    bin=""
    while num>0:
        bin+=str(num%base)
        num=num//base
    return bin[::-1]

num=int(input())
base=int(input())
print(decimal_conversion(num,base))