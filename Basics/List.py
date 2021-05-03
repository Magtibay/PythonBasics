friends = ["John" , "Stacy", "Jimbo", "Toby", "Stan" , "Toby"]
lucky_numbers = [3,7,19,23,45,69,420]

print(friends)
print(friends[0])
print(friends[1])
print(friends[2] + "\n")

print(friends[-1])
print(friends[-2])
print(friends[-3] + "\n")

print(friends[1:])
print(friends[1:3])

#find if toby is in the list
print(friends.index("Toby"))
print(friends.count("Toby"))

friends.sort()
print(friends)
lucky_numbers.reverse()
print(lucky_numbers)
# friends[1] = "Mike"
# print(friends[1])

# adds a list to another list
# friends.extend(lucky_numbers)
# print(friends)

# adds another item into the list
# friends.append("Creed")
# print(friends)

# adds item to the number position and pushes other items to the right
# friends.insert(1, "Kelly")
# print(friends)

# removes item from list
# friends.remove("Kelly")
# print(friends)

# clears the entire list
# friends.clear()
# print(friends)


