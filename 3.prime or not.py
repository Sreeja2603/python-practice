a=int(input("enter any number"))
counter=0
for i in range(1,a+1):
    if a%i==0:
        counter=counter+1
if counter>2:
    print("not prime")
else:
    print("prime")
