# Question 6
# Problem: Find the item with minimum discount
# Name: Vaibhavi Gupta
# Course: BTech DS + AI

def min_discount_item():
    n = int(input("Enter number of items: "))
    
    min_discount = float('inf')
    item_name = ""
    
    for i in range(n):
        data = input("Enter item,price,discount: ").split(',')
        name = data[0]
        price = int(data[1])
        discount = int(data[2])
        
        discount_amount = (price * discount) / 100
        
        if discount_amount < min_discount:
            min_discount = discount_amount
            item_name = name
    
    print(item_name)

min_discount_item()
