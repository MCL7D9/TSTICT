n=int(input("Input Number: "))
for i in range(n):
    for j in range(n):
        if j>=i and j<=(n-1-i):
            print("o",end="")
        else:
            print(" ",end="")
    print()