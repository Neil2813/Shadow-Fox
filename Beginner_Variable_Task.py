# 1. Create a variable named pi and store the value 22/7 in it. Now check the data type of this variable.

pi = (22/7)
print(type(pi))

# 2. Create a variable called for and assign it a value 4. See what happens and find out the reason behind the behavior that you see.
"""
for = 4
print(for)
"""
# The variable name 'for' is a reserved keyword in Python, which is why it raises a SyntaxError.

# 3. Store the principal amount, rate of interest, and time in different variables and then calculate the Simple Interest for 3 years. 
# Formula: Simple Interest = P x R x T / 100

principal_amount = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest: "))
time = 3
simple_interest = (principal_amount * rate_of_interest * time) / 100
print(f"The Simple Interest for {time} years is: {simple_interest}")
total_amount = simple_interest + principal_amount
print(f"The total amount after {time} years is : {total_amount}")
