# The item's discount and stock status have been defined
discounted = False
lowStock = True

# 1. Define a boolean variable moving product that is true
movingProduct = discounted or lowStock  # True

# 2. Create a boolean variable promotion
promotion = not movingProduct  # True if neither discounted nor low in stock

# Print the result
print("Is the item eligible for promotion?", promotion)