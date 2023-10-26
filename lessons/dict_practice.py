"""Practice with dictionary syntax."""

# Create a new dictionary
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print(ice_cream)

# Adding a key,value pair to a dictionary
ice_cream["mint"] = 3
print(ice_cream)

# Removing a key,value pair
ice_cream.pop("mint")
print(ice_cream)

# Accessing a value
print(ice_cream["chocolate"])

# Updating a value
ice_cream["vanilla"] = 10
print(ice_cream)

# Print the length
print(len(ice_cream))

# Using "in" in a conditional
if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("no orders of mint")

# Loop through dictionary
for key in ice_cream:
    # Print out <flavor> has <num orders> orders
    print(f"{key} has {ice_cream[key]} orders.")
