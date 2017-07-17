#### CLASS##########
#product_id = input("Please input a valid identifier:")
#print ("The product identifier is:" + str (product_id))



##below is professor's
#product_ids = []
#while True:
#    product_id = input("Please input a valid product identifier:")
#    if product_id == "DONE":
#        print("THANKS ALL DONE HERE")
#        break
#    else:
#        print("THE PRODUCT IDENTIFIER IS: " + str(product_id))
#        product_ids.append(product_id)

#print("OUTSIDE THE LOOP")
#print(product_ids)


### Project which I did is below...

import datetime

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
]

product_ids = []
while True:
    product_id = input("Please input a product identifier, or 'DONE' if there are no more items:")
    if product_id.strip() == 'DONE':
        break
    elif (int(product_id) > 20):
        print ("Choose between 1 to 20. Try again")
    elif (int(product_id)==0):
            print ("Choose between 1 to 20. Try again")
    else:
        product_ids.append(int(product_id))

print("SHOPPING CART ITEM IDENTIFIERS INCLUDE:", str(product_ids))

def lookup_product_by_id(product_id):
    matching_products = [product for product in products if product["id"] == product_id]
    # using list comprehension, creating list without creating empyt list
    return matching_products[0] # because the line above gives a list and we want to return a single item.


# PRINT RECEIPT

print("-------------------------------")
print("Hajime's GROCERY STORE")
print("-------------------------------")
print("Web: www.hajimegrocerystore.com")
print("Phone: 212-123-4567")
print("Checkout Time: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%m:%S"))

print("-------------------------------")
print("Shopping Cart Items:")

total = 0
for product_id in product_ids:
    product = lookup_product_by_id(product_id)
    total += product["price"] #total = total + product["price"]
    price_usd = ' (${0:.2f})'.format(product["price"])
    print(" + " + product["name"] + price_usd)
    #print product name, price, and calculate running_total (total price adding each price in product ID)

print("-------------------------------")
print("Subtotal:", '${0:.2f}'.format(total))
tax = total * 0.08875
print("Plus NYC Sales Tax (8.875%):", '${0:.2f}'.format(tax))
total2 = total + tax
print("Total:", '${0:.2f}'.format(total2))

print("-------------------------------")
print("Thanks for your business! Please come again.")
