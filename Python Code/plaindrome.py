number = int(input("Enter the number: "))
rev = 0
temp = number
while number!=0:
    digit = number%10
    rev = rev*10+digit
    number = number//10
if rev == temp:
    print("It is Plaindrome Number")
else:
    print("Not Plaindrome Number")