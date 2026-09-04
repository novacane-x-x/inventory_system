def display_inventory(inventory):#this a function to display the current inventory
    print('\nCURRENT INVENTORY')
    for product, quantity in  inventory.items():
        print(f'{product}:{quantity}')
def main():
#this is the main function to check the availability of a product and update the inventory
    inventory = {
        "Laptop": 5,
        "keyboard": 12,
        "mouse": 20,
        "Monitor": 7
        }
    display_inventory(inventory)#this updtates the inventory by calling the display_inventory function
#this allows the user top input a product  and chcks the availability of the product in the inventory
    product = input('\nEnter the product name to check availability: ').strip()
    if product not in inventory:
        print(f'{product} is not available in the inventory.')
        return
    if inventory[product] <= 0:
        print(f'{product} is out of stock.')
        return
    else:
        print(f'{product} is available with quantity: {inventory[product]}')
    """
 #this allows the user to input the quantity 
of the product sold and checks if the quantity 
sold is valid and updates the inventory accordingly
"""
    try:
        sold_quantity = int(input('\nEnter the quantity sold: '))
    except ValueError:
        print('Invalid input. Please enter a valid number.')
        return
    if sold_quantity < 0:
        print('Quantity sold cannot be negative.')
        return
    if sold_quantity > inventory.get(product, 0):
        print(f'Cannot sell {sold_quantity} units of {product}. Only {inventory.get(product, 0)} available.')  
        return
    inventory[product] -= sold_quantity#updates the inventory.
    display_inventory(inventory)#displays the updated inventory after the sale
if __name__ == "__main__":#this checks if the script is being run directly and calls the main function
    main()#if also prevents the main function from being executed when the script is imported as a module in another script.
