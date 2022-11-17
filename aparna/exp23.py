str=input("Enter the string:")
dict={}
line=str.split( )
print(line)
for word in line:
    if word in dict:
        dict[word]=dict[word]+1
    else:
        dict[word]=1
print("character frequency")
for m,n in dict.items():
    print(m,n)
