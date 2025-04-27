"""
Create a list of your friends' names. The list should have at least 5 names.
Create a list of tuples. Each tuple should contain a friend's name and the length
of the name.
For example, if someone’s name is Aditya, the tuple would be: ('Aditya', 6)
"""
friends = ["Aarav", "Priya", "Rohan", "Meera", "Siddharth"]

friends_with_length = [(friend, len(friend)) for friend in friends]

print(friends_with_length)
