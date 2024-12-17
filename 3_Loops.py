# Loops are used for repetitive execution of a block of code.
# In Python, we primarily use two types of loops: 1- for loop 2- while loop.

# 1- For Loop

for n in range(1, 6):   # here n is Loop Variable
    print(f"Current number is: {n}")

#The range() function in Python is used to generate a sequence of numbers. It is often utilized in loops, particularly with for loops, to specify the number of iterations.

# The for loop can also be used to iterate over a sequence (like a list, tuple, or string).
for n in "fruits": 
    print(n)


# 2- While Loop

# The while loop continues to execute a block of code as long as a specified condition is True. e.g count < 5
count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1  # Increment count by 1 each iteration
