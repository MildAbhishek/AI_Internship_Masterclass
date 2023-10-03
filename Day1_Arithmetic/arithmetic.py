a=5
b=6
c=a+b
d=a-b
e=a*b
print(a)
print("Hello Everyone")
print(a,b,c,d,e)

if a<b:
    print("a is less than b")
elif a==b:
    print("a is equal to b")
    if c<=a:
        print("c is less than a")
    else:
        print("c is not less than a")
else:
    print("b is less than a")




for i in range(1, 10, 2):
    print(i)

i= 0;
while i<10:
    print(i)
    i += 1
