"""
3. Write a program to check if two cities belong to the same country. Ask the user to enter two cities and print whether they belong to the
same country or not.
Example:
Enter the first city: "Mumbai"
Enter the second city: "Chennai"
Output: "Both cities are in India"
Example:
Enter the first city: "Sydney"
Enter the second city: "Dubai"
Output: "They don't belong to the same country"
"""

Australia = ["Sydney" , "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore" , "Chennai", "Delhi"]
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")
if city1 in Australia and city2 in Australia:
    print(f"Both cities are in Australia")
elif city1 in UAE and city2 in UAE:
    print(f"Both cities are in UAE")
elif city1 in India and city2 in India:     
    print(f"Both cities are in India")
elif city1 in Australia and city2 in UAE:
    print("They don't belong to the same country")
elif city1 in Australia and city2 in India:
    print("They don't belong to the same country")
elif city1 in UAE and city2 in Australia:
    print("They don't belong to the same country")
elif city1 in UAE and city2 in India:
    print("They don't belong to the same country")
elif city1 in India and city2 in Australia:
    print("They don't belong to the same country")
elif city1 in India and city2 in UAE:
    print("They don't belong to the same country")
else:
    print("One or both cities are not in the list of countries")