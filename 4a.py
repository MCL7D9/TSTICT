n=int(input("How many levels?"))
for i in range(n):
    for j in range(i):
        print("x",end="")
    for j in range(n-i):
        print("o",end="")
    print()
        