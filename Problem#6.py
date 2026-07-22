#Prime number Check 
num = int(input("Enter a number: "))
if num <= 1:
    print("Not a Prime number")
else: 
    is_prime = True
    count = num - 1 
    while count > 1:
        if num % count == 0:
            is_prime = False
            break
        count -= 1
    if is_prime:
        print("Prime number")
    else: 
        print("Not a Prime number")