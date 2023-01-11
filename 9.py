a=input("enter the term: ")
b=input("enter the term: ")
c=a.split()
d=b.split()
e=[]
for i in c:
        if i not in d:
                e.append(i)
for i in d:
        if i not in c:
                e.append(i)
print(e)
