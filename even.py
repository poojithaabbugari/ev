num=int(input("Enter a number"))  #We are taking the input as integer from the user

if num % 2 == 0:  #if the given number is divisible by 2 and gives the remainder as zero then it is considered as even number
    print("It is even") #print is a function,if the above condition is true,then it prints it is even,if the condition is wrong then it goes to the else part
else: #it does consist  of any condition,just else part
    print("It is odd")