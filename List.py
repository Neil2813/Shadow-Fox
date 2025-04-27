"""
1.  have a list of superheroes representing the JusticeLeague.
justice_league = ["Superman" , "Batman" , "Wonder Woman" , "Flash" , "Aquaman" , "Green Lantern"]
Perform the following tasks:
1. Calculate the number of members in the Justice League.
2. Batman recruited Batgirl and Nightwing as new members. Add them to your list.
3. Wonder Woman is now the leader of the Justice League.Move her to the beginning of the list.
4. Aquaman and Flash are having conflicts, and you need to separate them. Choose either "Green Lantern" or "Superman" and move them in between 
Aquaman and Flash.
5. The Justice League faced a crisis, and Superman decided to assemble a new team. Replace the existing list with the following
new members: "Cyborg" , "Shazam" , "Hawkgirl" , "Martian Manhunter", "Green Arrow".
6. Sort the Justice League alphabetically. The hero at the 0th index will become the new leader.
(BONUS: Can you predict who the new leader will be?)
Your task is to write Python code to perform these operations on the "justice_league" list. Display the list at each step to observe
the changes.
"""
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Step 1:", justice_league)

print("Step 2:", len(justice_league))

justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("Step 3:", justice_league)

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Step 4:", justice_league)

aquaman_index = justice_league.index("Aquaman")
justice_league.remove("Superman")
justice_league.insert(aquaman_index + 1, "Superman")
print("Step 5:", justice_league)

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("Step 6:", justice_league)

justice_league.sort()
print("Step 7:", justice_league)

print("New Leader:", justice_league[0])
