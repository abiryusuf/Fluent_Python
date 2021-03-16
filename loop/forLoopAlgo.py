# Question 2
# Fill in the blanks to make the factorial function return the factorial of n. 
# Then, print the first 10 factorials (from 0 to 9) with the corresponding number. 
# Remember that the factorial of a number is defined as the product of an integer and 
# all integers before it. For example, the factorial of five (5!) is equal to 1*2*3*4*5=120. 
# Also recall that the factorial of zero (0!) is equal to 1.
def factorial(n):
    result = 1
    for x in range(1, n + 1):
        result = result * x
    return result

for n in range(0,9):
    print(n, factorial(n+1))
# Question 3
# Write a script that prints the first 10 cube numbers (x**3), starting with x=1 and ending with x=10.

for x in range(1, 11):
    print(x**3)


# Question 4
# Write a script that prints the multiples of 7 between 0 and 100. 
# Print one multiple per line and avoid printing any numbers that aren't multiples of 7. 
# Remember that 0 is also a multiple of 7.
a = range(0, 100)

for num in range(1,100):
    if num % 7 == 0:
        print(num)