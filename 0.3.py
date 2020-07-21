x = [6.465, 855.54, 75.43, 9, 5.234, 9.946, 645.74, 435.34]
y = float("-inf")
for i in x:
    i = int(i)
    if i > y and i % 5 == 0:
        y = i
print(y)

