try:
    int1 = int(input("enter integer 1:"))
    int2 = int(input("enter integer 2:"))
    sum = int1 + int2
    print(sum)
except ValueError:
    print("please enter a valid integer")    

