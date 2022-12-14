n=int(input("enter no. of rows"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("")
print("==================")
for i in range(n+1,0,-1):
    for j in range(1,i):
        print("*",end=" ")
    print(" ")
print("==================")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print(" ")
print("==================")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print(" ")
