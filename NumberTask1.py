"""
Write a function that takes two arguments, 145 and 'o', and uses the `format` function to return a formatted string. Print the result.
Try to identify the representation used.
"""
def format_number(num, fmt):
    formatted = format(num, fmt)
    return formatted

result = format_number(145, 'o')
print("Formatted result:", result)

# o tells the compiler to convert the number to octal representation.
