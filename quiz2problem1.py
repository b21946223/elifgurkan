import sys

a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]

discriminant = b ** 2 - 4 * a * c
delta = (b ** 2 - 4 * a * c) ** 0.5

if discriminant > 0:
    print("There are two solutions")
    root1 = (-b + delta) / 2 * a
    root2 = (-b - delta) / 2 * a
    print('Solutions(s): ' + '{0:.2f}'.format(root1), end=" ")
    print('{0:.2f}'.format(root2))

elif discriminant == 0:
    print("There is one solution")
    root = -b / 2 * a
    print('Solution(s): ' + '{0:.2f}'.format(root))

else:
    print("There is no solution in real numbers")


