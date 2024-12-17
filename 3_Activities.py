# Take 5 integer values from user and display their sum.

sum = 0
count = 0
while count <= 4:
    num = int( input("Enter a number: "))
    sum = sum + num
    count = count + 1

print("Sum = ", sum)

