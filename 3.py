a=input("enter the 1 sentences: ")
b=input("enter the 2 sentences: ")
c=a.split()
d=b.split()
x=[]
for i in c:
    if i not in d:
        x.append(i)
for i in d:
    if i not in c:
        x.append(i)
print(x)
    
