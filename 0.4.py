import random

x=float("inf")
s=0

for i in range(10):
    i = random.randint(0, 100)
    if i > x:
        s += 1
    x = i

print("количество: ", s)