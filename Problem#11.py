# Check if a number is Palindrome or not
num = int(input("Enter a number: "))
temp = num
new_num = 0 
while num > 0 :
    remainder = num % 10
    new_num = new_num * 10 + remainder
    num = num // 10
if new_num == temp:
    print("The number is Palindrome")
else: 
    print("The number is not Palindrome")