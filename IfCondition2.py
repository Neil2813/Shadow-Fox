"""
Write a program to determine which country a city belongs to. Given
list of cities per country:
Australia = ["Sydney" , "Melbourne" , "Brisbane" , "Perth"]
UAE = ["Dubai" , "Abu Dhabi" , "Sharjah" , "Ajman"]
India = ["Mumbai" , "Bangalore" , "Chennai" , "Delhi"]
Ask the user to enter a city name and print the corresponding country.
Example:
Enter a city name: "Abu Dhabi"
Output: "Abu Dhabi is in UAE"
"""

Australia = ["Sydney" , "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore" , "Chennai", "Delhi"]
city =input("Enter the city name: ")
if city in Australia:
    print(f"{city} is in Australia")
elif city in UAE:
    print(f"{city} is in UAE")
elif city in India:
    print(f"{city} is in India")
else:
    print(f"{city} is not in the list of countries")