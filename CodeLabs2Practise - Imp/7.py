# Given list of locations
# Given list of locations
locations = ['dubai', 'paris', 'switzerland', 'London', ' amsterdam', 'New York']

# Print the original list
print("Original list:")
print(locations)


# Find and print the length of the list
print("\nLength of the list:", len(locations))

# Use sorted to print the list in alphabetical order without modifying the original list
print("\nList in alphabetical order (without modifying the original list):")
print(sorted(locations))

# Show that the original list is still in its original order
print("\nOriginal list after using sorted:")
print(locations)


# Use sorted to print the list in reverse alphabetical order without changing the original list
print("\nList in reverse alphabetical order (without modifying the original list):")
print(sorted(locations, reverse=True))

# Show that the original list is still in its original order
print("\nOriginal list after using sorted in reverse:")
print(locations)

# Use reverse to change the order of the list
locations.reverse()
print("\nList after using reverse:")
print(locations)

# Use sort to change the list so it's stored in alphabetical order
locations.sort()
print("\nList after using sort (alphabetical order):")
print(locations)