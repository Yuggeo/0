import random

x=float("inf")
a=float("inf")
b=float("inf")
c=float("inf")

s=0

for i in range(10):
    i = random.randint(0, 100)
    if c>b<a:
        s += 1
    i = a
    c = b 
    b = a
    print(i)
print("количество: ", s)
