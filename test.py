L=['Bart','Lisa','Adam']
for x in L:
	print('hello', x)

h=hex
a=h(255)
b=h(1000)
print(a)
print(b)

import math

def quadratic(a, b, c):
	delta = (b ** 2) - 4 * a * c
	delta_sqrt = math.sqrt(delta)
	if delta > 0:
		x = (-b + delta_sqrt) / (2 * a)
		y = (-b - delta_sqrt) / (2 * a)
		return (x, y)
	elif delta < 0:
		return None
	else:
		return -b / (2 * a)

print(quadratic(1, 3, -4))
print("Hello")

