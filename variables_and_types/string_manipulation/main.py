grocery_items = "milk cheese bread apples oranges chicken"
grocery_items[0:5]
dairy1 = "milk"
dairy2 = "cheese"
bakery1 = "bread"
aisle = 5

# Embed multiple variables in one message 

# 1) Extract the items via slicing
dairy1 = grocery_items[0:4]   # "milk"
dairy2 = grocery_items[5:11]  # "cheese"
bakery1= grocery_items[12:17] # "bread"
aisle  = 5

# 2) Build and print the message
message = f"We have dairy and bakery items: {dairy1}, {dairy2}, and {bakery1} in aisle {aisle}"
print(message)