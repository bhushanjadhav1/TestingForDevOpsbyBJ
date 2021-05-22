a=int(input("Enter number 1 "))
b=int(input("Enter number 2 "))
c=int(input("Enter number 3 "))
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if (i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])
            
