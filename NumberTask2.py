"""
In a village, there is a circular pond with a radius of 84 meters. Calculate the area of the pond using the formula: Circle Area = πr^2. 
(Use the value 3.14 for π) Bonus Question: If there is exactly 1.4 liters of water in a square meter, what is the total amount of water in the 
pond? Print the answer without any decimal point in it. Hint: Circle Area = π r^2 Water in the pond = Pond Area Water per Square Meter
"""

radius = 84
pi = 3.14
pond_area = pi*radius**2
print(f"The area of the pond is: {pond_area} square meters")
water_per_square_meter = 1.4
total_water = water_per_square_meter*pond_area
total_water = int(total_water)
print(f"The total amount of water in the pond is: {total_water} liters")
