import random
min_value = -1000
max_value = 1000


for i in range(10):
    i = random.randint(-1000, 1000)
    if i > min_value:
        min_value = i
    elif i < max_value:
        max_value = i

    a = (min_value + max_value)/2

print(min_value, max_value)
print(a)
