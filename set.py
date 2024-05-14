a={1,2,3,4,5,5}
# still print 5 one time no duplicate allowed
b={3,4,5,6,7}
print(a)
print(b)
print("Union of 2 set",a|b)
print("Intersection of 2 set",a&b)
print("Difference of 2 set",a-b)
print("symmetric difference of 2 set",a^b)
# a[2]=10 not allowed in case of set 
print(type(a))
