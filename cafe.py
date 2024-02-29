# create menu
menu = ["Coffee", "Cake", "Tea", "Muffin"]
print(menu)

# now to create dictionaries with stock and value

inventory = [("Coffee", 20), ("Cake", 10), ("Tea", 15), ("Muffin", 8)]
stock = dict(inventory)

price = {"Coffee" : 2.5,
              "Cake" : 4,
              "Tea" : 2,
              "Muffin" : 3.5
              }

# dictionaries created, now to calculate total stock worth

coffee_value = (stock["Coffee"] * price["Coffee"])
cake_value = (stock["Cake"] * price["Cake"])
tea_value = (stock["Tea"] * price["Tea"])
muffin_value = (stock["Muffin"] * price["Muffin"])

total_stock = int(coffee_value + cake_value + tea_value + muffin_value)

print ("The total value of stock is " + str(total_stock) )