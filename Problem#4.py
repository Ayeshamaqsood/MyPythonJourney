#Take a number and print its table till 10.
num = int(input("Enter the number:"))
for i in range(1,11) : # step 1 is automatic 
    product = num * i;
    print(f"{num} * {i} = {product}")