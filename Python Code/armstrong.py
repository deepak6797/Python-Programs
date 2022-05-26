number = int(input("Enter the number: "))
temp = number
power = len(str(number))
sum = 0
while number!=0:
    digit = number%10
    sum = sum + (digit ** power)
    number = number//10
if temp == sum:
    print("It's Armstrong Number")
else:
    print("Not Armstrong number")