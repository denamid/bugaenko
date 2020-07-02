import random

random_1 = []
random_2 = []

random_3 = []

for i in range(0, 10):
	n = random.randint(1, 20)
	random_1.append(n)
print(f"первая строка случайных чисел = {random_1}")

for i in range(0, 10):
	n = random.randint(15, 25)
	random_2.append(n)
print(f"вторая строка случайных чисел = {random_2}")

random_3 = random_1 + random_2
print(f"1+2 список = {random_3}")
random_3.clear()

random_3 = list(random_1)
random_3.extend(i for i in random_2 if i not in random_3)

print(f"1+2 без повторений = {random_3}")
random_3.clear()
random_3 = list(set(random_1).intersection(random_2))

print(f"1+2 только повторения чисел двух списков = {random_3}")
random_3.clear()

temp_lst = (random_1 + random_2)

for x in temp_lst:
	if x not in random_1 or x not in random_2:
		random_3.append(x)

print(f"1+2 только уникальные элементы списков = {random_3}")
random_3.clear()

random_lst = sorted(random_1)
random_lst2 = sorted(random_2)

tup = (random_1[0], random_1[-1], random_2[0], random_2[-1])
random_3 = list(tup)

print(f"минимальные и максимальные значения обеих списков = {random_3}")