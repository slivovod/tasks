import random

num_1 = int(random.randint(0, 36))
num_2 = float(random.uniform(2, 256))
num_3 = int(random.randint(-8, 32))
num_4 = float(random.uniform(-144, 240))

exp1 = ((num_1 + num_2) / num_3) * num_4
exp2 = (num_3 * num_4) - (num_2 // num_1)
exp3 = (num_1 / (num_4 - num_3)) + num_2

print("expression 1: ", exp1)
print("expression 2: ", exp2)
print("expression 3: ", exp3)