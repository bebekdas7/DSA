# pyramid pattern

n = 4

for i in range(4):
    space = n - i + 1
    for j in range(space):
        print(" ", end=" ")
    for k in range(2 * i + 1):
        print("*", end=" ")
    print()