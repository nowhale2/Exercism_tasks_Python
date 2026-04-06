def add_item(current_cart, items_to_add):
    """Add items to shopping cart.
 
    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for el in items_to_add:
        if el in current_cart:
            current_cart[el] += 1
        else:
            current_cart.setdefault(el, 1)
    return current_cart
  
def read_notes(notes):
    """Create user cart from an iterable notes entry.
 
    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    new_dict = dict.fromkeys(notes, 1)
    return new_dict
  
def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.
 
    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    for update in recipe_updates:
        recipe_name, recipe_data = update
        ideas[recipe_name] = recipe_data
    
    return ideas
  
def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.
 
    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return sorted(cart.items())
  
def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.
 
    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    order_basket = {}
    
    for item, quantity in cart.items():
        if item in aisle_mapping:
            aisle_number, needs_cooling = aisle_mapping[item]
            order_basket[item] = [quantity, aisle_number, needs_cooling]
    
    
    return sorted(order_basket.items(), key=lambda x: x, reverse=True)
  
def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.
 
    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    store_inventory_update = {}
    for key, value in store_inventory.items():
        if key in fulfillment_cart:
            if isinstance(store_inventory[key][0], int):
                if store_inventory[key][0] - fulfillment_cart[key][0] != 0:
                    store_inventory_update[key] = [store_inventory[key][0] - fulfillment_cart[key][0], store_inventory[key][1], store_inventory[key][2]]
                else:
                    store_inventory_update[key] = ['Out of Stock', store_inventory[key][1], store_inventory[key][2]]
            else:
                store_inventory_update[key] = store_inventory[key]
        else:
            store_inventory_update[key] = store_inventory[key]
    return store_inventory_update
