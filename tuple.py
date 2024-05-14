Mytuple=('hi','hello','bye','see')
print(Mytuple)
print(Mytuple[0])
print(Mytuple[-2])
print(Mytuple[1:3])
print(Mytuple[:3])
print(Mytuple[2:])
# creating tuple with 1 element
tuple2=("itika",)
print(type(tuple2))

tuple3=("lamba")
print(type(tuple3))

# change value of a tuple
a=(1,2,3,4,5)
b=list(a)
b.append(8)
a=tuple(b)
print(a)

# unpack tuples
(hi,*hello)=a
print(hi)
print(hello)

#traverse
for x in a:
 print(x)

