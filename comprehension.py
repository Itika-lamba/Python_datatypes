ls=[1,2,3,4,5,6]
ans=[x for x in ls if(x%2)==0]
print(ans)

ans2=[x*x for x in range(1,10)]
print(ans2)

# dict
ans3={x:x**2 for x in range(1,5)}
print(ans3)
print(type(ans3))

# use of zip 
a=["india","USA"]
b=["delhi","abc"]
ans4={key:val for key,val in zip(a,b)}
print(ans4)