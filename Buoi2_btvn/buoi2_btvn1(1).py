a = float(input())
b = float(input())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a**b)
if a > b:
    print("a>b")
elif a < b:
    print("a<b")
else:
    print("a=b")
print(int(a) & int(b))
print(int(a) | int(b))
print(int(a) ^ int(b))
print(not (a == b))
print(int(a) >> 5)
print(int(a) << 6)
print(bin(int(a))[2:][::-1])