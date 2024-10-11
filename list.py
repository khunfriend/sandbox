x = input().split()
h1 = int(x[0])
m1 = int(x[1])
s1 = int(x[2])
h2 = int(x[3])
m2 = int(x[4])
s2 = int(x[5])
if[h1,m1,s1] < [h2,m2,s2] :
    print("Yes")
else:
    print("NO")