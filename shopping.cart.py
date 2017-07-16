
#--->> python3 shopping_cart.py
#Please input a product identifier, or 'DONE' if there are no more items: 2
#Please input a product identifier, or 'DONE' if there are no more items: 18
#Please input a product identifier, or 'DONE' if there are no more items: 2
#Please input a product identifier, or 'DONE' if there are no more items: 6
#Please input a product identifier, or 'DONE' if there are no more items: 8
#Please input a product identifier, or 'DONE' if there are no more items: DONE
#-------------------------------
#MY GROCERY STORE
#-------------------------------
#Web: www.mystore.com
#Phone: 1.123.456.7890
#Checkout Time:  2017-07-12 20:07:46
#-------------------------------
#Shopping Cart Items:
# + All-Seasons Salt ($4.99)
# + Pizza for One Suprema Frozen Pizza ($12.50)
# + All-Seasons Salt ($4.99)
# + Dry Nose Oil ($21.99)
# + Cut Russet Potatoes Steam N' Mash ($4.25)
#-------------------------------
#Subtotal: $48.72
#Plus NYC Sales Tax (8.875%): $4.32
#Total: $53.04
#-------------------------------
#Thanks for your business! Please come again.


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
product_ids = []
while True:
    product_id = input("Please input a product identifier, or 'DONE' if there are no more items:")
    if product_id.strip() == 'DONE':
        break
    else:
        product_ids.append(int(product_id))

print("SHOPPING CART ITEM IDENTIFIERS INCLUDE:"+ str(product_ids))
