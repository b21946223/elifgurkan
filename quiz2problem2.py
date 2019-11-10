import sys

def evennumber():
	even = []
	count1 = 0
	count2 = 0

	l = list(map(int, sys.argv[1].rstrip().split(",")))

	for i in l:
		if int(i) > 0:
			if i % 2 == 0:
				even.append(i)
	for i in l:
		if int(i) > 0:
			count1 = count1 + i
	for i in even:
		count2 = count2 + i

	print("Even Numbers: ", end="")
	print(even)
	print("Sum of Even Numbers: " + str(count2))
	print("Even Number Rate: " + str('{0:.{1}f}'.format((count2 / count1), 3)))




