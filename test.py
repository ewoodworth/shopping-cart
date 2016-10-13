import melons

cart = {"golh" : 2, "meli" : 3}

purchases = []
total_cost = 0

for key in cart.keys():
    purchases.append(key)

for key, value in melons.melon_types.items():
    if key in purchases:
        order_price = cart[key] * float(melons.melon_types[key].price)
        total_cost += order_price
        melons.melon_types[key].quantity = cart[key] 
        melons.melon_types[key].total_cost = order_price
        purchases.append(melons.melon_types[key])

print purchases, total_cost

        # melon_name = melon_types[melon_id][2]
        # price = value * melon_types[melon_id][3]  
        # total_cost += price
        # melon_id.quantity = value
        # melon_id.total_cost = price 
        # purchases.append(melons.melon_id) 


    # - get the cart dictionary from the session
    # - create a list to hold melon objects and a variable to hold the total
    #   cost of the order
    # - loop over the cart dictionary, and for each melon id:
    #    - get the corresponding Melon object
    #    - compute the total cost for that type of melon
    #    - add this to the order total
    #    - add quantity and total cost as attributes on the Melon object
    #    - add the Melon object to the list created above
    # - pass the total order cost and the list of Melon objects to the template
    #
    # Make sure your function can also handle the case wherein no cart has
    # been added to the session