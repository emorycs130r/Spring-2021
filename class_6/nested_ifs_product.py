itemsOrdered = 30
itemsInStock = 32

print("Got an order for", itemsOrdered, "items. In stock:", itemsInStock)

# Compare order size against inventory
if itemsOrdered >= itemsInStock:
    print("Resupply the inventory. We're running out!")
else:
    packageCount = round(itemsOrdered / 8)

    if packageCount > 1:
        print("We need multiple packages to fulfil this order!")