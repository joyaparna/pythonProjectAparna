d={1:4,5:6,2:6}
sorted_d=sorted(d.items())
print(sorted_d)
print('dictionary in ascending order by value:',sorted_d)
sorted_d=sorted(d.items(),reverse=True)
print('dictionary in decending order by value:',sorted_d)