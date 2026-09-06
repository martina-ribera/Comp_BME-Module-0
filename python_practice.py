# This is your first coding assignment for Computational BME.
# As discussed in class, feel free to use AI tools to help you complete this assignment, but remember to cite them.
# I encourage you to try the problems yourself first and only use AI tools when you are stuck to benefit your learning. 

# %% ###########################################################
# Problem 1: Practice writing pseudocode

# Write pseudocode that will input a integer N and output the sum of the first N numbers in the fibonacci sequence.
# Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Example: If N = 5, the output should be 0 + 1 + 1 + 2 + 3 = 7

""" # you can use three double-quotes to write multi-line comments
XXX Write your pseudocode here XXX


input integer N
Make first_number = 0
make second_number = 1
make total = 0

repeat n times
    add first_number to total
    make following_number = first_number + second_number
    make first_number = second_number
    make second_number = following_number
print total
"""

# %% ###########################################################
# Problem 2: Comment your code
# Comments are very helpful for others (especially when pair-coding!) and yourself to understand your code! Add comments to the following code, which will run but produces the wrong output. Once you comment the code, you should be able to identify the error and fix it (the correct total that should be printed is 12).
N = 6 

a = 0 # set a to the first fibonacci number
b = 1 # set b to the second fibonacci number
count = 0 #keep count of how many times the loop runs
total = 0

while count < N:
    total = total + a # instead of 'b', it needs to be 'a' because we want to add the current fibonacci number to the total

    next_value = a + b #new fibonacci number
    a = b # update a to what b's fibonnaci number was
    b = next_value # update b to next fibonacci number

    count = count + 1

print(total)

# %% ###########################################################
# Problem 3: Using common Python libraries
# What is the standard deviation of the first 10 numbers in the fibonacci sequence? Use the numpy library to calculate the standard deviation.
import numpy as np
fib_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] # first 10 fibonacci numbers
standard_dev = np.std(fib_numbers) # calculates the standard dev with numpy's std function (had to google this, didn't know how to find or execute the standard deviation function in numpy)
print("The standard deviation of the first 10 fibonacci numbers is: ", standard_dev)

# %% ###########################################################
# Problem 4: Don't repeat yourself by writing functions
# Write a function that takes an integer N as input and returns the sum of the first N numbers in the fibonacci sequence.
# Then use this function to calculate the sums for N = 5, 10, 15, 20, 25, and 30 and print them as a list.

#neeed to set function before calling any values
def fibonacci_sum(N): # take the sum of N fibonacci numbers
    a = 0 # set a to first fib number
    b = 1 # set b to the second fib number
    count = 0 #count how many times loop runs
    total = 0

    while count < N:
        total = total + a # instead of 'b', it needs to be 'a' because we want to add the current fibonacci number to the total

        next_value = a + b #new fibonacci number
        a = b # update a to what b's fibonnaci number was
        b = next_value # update b to next fibonacci number

        count = count + 1

    return total #send total back to function call and exit function

N_values = [5,10,15,20,25,30] # list of N values required

sums = [] # empty list to store sums

for each in N_values: #make the loop for each value in N_values 
    answer = fibonacci_sum(each)
    sums.append(answer) # add answer to sums list
# used ai to simplify thiis code section and explain the "for... in..." loop, bc i had forgotten how to do it
print(sums)


# %% ###########################################################
# Problem 5: Read your error messages
# Run the following code block to see what the error messages are. Then, for each error:
# 1. Identify what type of error it is (SyntaxError, NameError, TypeError, etc.)
# 2. Add a comment to the line that is throwing the error explaining what the error is
# 3. Fix the error so that the code runs correctly

# You will only see one error at a time when you run the code. After fixing one error, run the code again to see the next error. Your final code should work correctly and will have comments where the original errors were.


def find_fib_above_limit(limit):
    """# The function inputs an integer called "limit" and finds the first number that goes above "limit" in the fibonacci sequence. It returns the index of that number.
    :param limit: limit of fibonacci sequence
    :type limit: integer
    :return: index of the first number above limit
    :rtype: integer
    """
    a = 0 # TypeError bc both 'a' and 'b' values cannot be strings, they need to be integeers in order for the loop to properly process the fibonacci nums
    b = 1 # 'limit' is an integer, so a and b need to be integers as well
    index = 0 # NameError because index was called in the loop below but it wasnt a defined variable
     
    while a <= limit:
        next_value = a + b
        a = b
        b = next_value
        index += 1

    return index


result = find_fib_above_limit(20)
print("The index of the first number above your limit is: ", result)
# %% ###########################################################
# Problem 6: Test your code
# The following function will run but will output the wrong answer sometimes. Add test cases to verify that the function works correctly for a variety of inputs. If you find any inputs that produce incorrect outputs, fix the function. The function, when working properly, should return the sum of all odd Fibonacci numbers less than or equal to the input "limit".
### did you mean even instead of odd? the function is called sum_even_fib and the code checks for even numbers, so I will assume you meant even.

def sum_even_fib(limit):
    a = 0
    b = 1 #setting a and b to first two fibonacci numbers
    total = 0
    while b <= limit: # loop runs until fib number greater than limit
        if b % 2 == 0:  #checks if Fibonacci number is even
            total = total + b #dont replace total with b, need to add even number to entire total
        a = b
        b= a + b #move to next fib number
    return total


# Add your test cases here
limit = 50 # test number, i fiddled around and put in a bunch of diferent onces and it seems to work
result = sum_even_fib(limit)
print("The sum of all even Fibonacci numbers less than or equal to", limit, " is:", result)
# used ai to help me udnerstad what was being asked of me in this problem, and to find an error I was facing in my function regarding what the total was supposed to be equal to  (line 135)
# %%

