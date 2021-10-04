import random

a = random.randint(1, 144)
b = random.uniform(0.1, 24)
c = random.randint(1, 240)
d = random.randint(1, 12)
e = random.uniform(1, 16)

m = random.randint(1, 4)

n = ((a * (c - d)) + e) / (b * 2**m)
print(n)