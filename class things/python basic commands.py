print("You can make a list of values:")
x = [0, 1, 2, 3, 4]
y = [5, 6, 7, 8, 9, 10, 11]
print(f"  {x = }")
print(f"  {y = }")
print()

print("You can concatenate lists (i.e., join them) by adding them:")
z = x + y
print(f"  {z = }")
print()

print("You can access elements in a list via their index:")
print(f"  {z[0] = }")  # Access the 1st value in the list.
print(f"  {z[1] = }")  # Access the 2nd value in the list.
print(f"  {z[-1] = }")  # Access the last value in the list.
print(f"  {z[-2] = }")  # Access the 2nd last value in the list.
print()

print("You can access a slice of a list by various methods:")
print(f"  {z[2:4] = }")  # Start at idx=2, stop before idx=4.
print(f"  {z[1:10:2] = }")  # Start at idx=1, stop before idx=10, in steps of 2.
print(f"  {z[::-1] = }")  # All indices, in steps of -1. This reverses the list.
print()