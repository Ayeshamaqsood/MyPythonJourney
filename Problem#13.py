# Find Factorial of a Number 
# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, num+1):
#         factorial *= i
# print(f"Factorial of the {num} is {factorial} ")

num = int(input("Enter a number: "))
original = num 
factorial = 1

while num > 0:
    factorial *= num
    num -= 1
print(f"Factorial of the {original} is {factorial} ")

