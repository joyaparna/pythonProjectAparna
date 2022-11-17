n=int(input("enter the number of list"))
print("enter the list elements")
list=[]
for i in range(0,n):
    a=int(input())
    if(a>100):
         list.append("over")
    else:
         list.append(a)
print(list)