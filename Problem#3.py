# Take three numbers and find the largest.
First_num = int(input("Enter your First number:"))
Sec_num = int(input("Enter your Second number:"))
Third_num = int(input("Enter your Third number:"))
if First_num >Sec_num and First_num  >Third_num : 
        print(f"{First_num} is largest of all.")
elif Sec_num> First_num and Sec_num> Third_num:
        print(f"{Sec_num} is largest of all.")
else :
     print(f"{Third_num} is the largest of all.")