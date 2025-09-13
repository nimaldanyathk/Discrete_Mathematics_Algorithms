def power(a,n):
    if n==0:
        return 1
    
    #Recursive case: a^n=a*a(n-1)
    else:
        return a*power(a,n-1)
    
x=int(input("Enter the number"))
y=int(input("Enter the power"))
result=power(x,y)
print(f"{x} raised to the power of {y} is {result}")
