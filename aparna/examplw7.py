n=int(input("enter the limit:"))
list=int(input("enter the elements:"))
list=[]
for i in range(0,n):
    x=int(input())
     if x<0:
        list.append(x)
        list.remove(x)
     else:
        list.append(x)
print(list)