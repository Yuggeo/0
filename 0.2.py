x = [0, 2,  -100, 200, 1000, -1000, 5, 3, 4, 10, 15, -10000000 ]
y = float("inf")

for i in x:
    if i > 0 and i < y:
        y = i
print(y)