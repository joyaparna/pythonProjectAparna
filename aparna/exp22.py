str=input("enter the sting:")
dict={}
for n in str:
    if n in dict:
        dict[n]=dict[n]+1
        print(dict)
    else:
        dict[n]=1
        print(dict)
print("character freqency:")
for m,n in dict.items():
    print(m,n)