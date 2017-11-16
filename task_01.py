def sort(a):
	for i in range(1, len(a)):
		for o in range(i):
			if a[i - o] < a[i - o - 1]:
				a[i - o], a[i - o - 1] = a[i - o - 1], a[i - o]
			else:
				break
	return a
a = [5,4,3,2,1]

a = sort(a)
print(a)