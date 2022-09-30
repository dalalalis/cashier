

def get_invoice_items(items):
    invoice_items=[]
    for item in items:
        inputitem= input("Item (enter 'done' when finished")
        price= int (input("price:"))
        quantity= int (input(" quantity:"))
        item={"item":inputitem,"price": price,"quantity":quantity}
        return invoice_items.append[item]
    if inputitem== "done":
        return invoice_items 

    

            
    # Items is a dictionary with a quantity and price key, and a name key
    # Return a list of all the invoice line items in the following format:
    # quantity name subtotal currency
    # For example, if we had the following:
    # [
    #   {'name': 'Apple', 'quantity': 1, price: 0.2 },
    #   {'name': 'Orange', 'quantity': 4, price: 0.3 },
    # ]
    # We should return the following:
    # ['1 Apple 0.200KD', '4 Orange 1.200KD']
    # ---
    # Write your code here
    


def get_total(items):
    total= 0
    for item in items:
        subtotal= item["quantity"] *item["price"]
        total= total+ subtotal
        return total 
    # Items is a dictionary with a quantity and price key
    # Calculate the total of all items in the cart
    # Write your code here
    


def print_receipt(invoice_items, total):
    # invoice_items will be the list of formatted items received from
    # `get_invoice_items`, and total will be a float. Print out a nice receipt
    # displaying a title, all the invoice items on separate lines, and the
    # total at the end.
    # ---
    # Write your code here
    print ("-------")
    print("reciept")
    print("---------")
    
    




def main():
    # Write your main logic here
    ...


if __name__ == "__main__":
    main()
