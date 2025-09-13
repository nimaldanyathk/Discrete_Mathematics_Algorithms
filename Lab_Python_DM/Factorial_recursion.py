def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial(n - 1) 

x = int(input("Enter the number: "))
print(f"Factorial of {x} is {factorial(x)}")