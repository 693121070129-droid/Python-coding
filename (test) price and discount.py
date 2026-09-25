while True:
    price = float(input("Enter the price of the item: "))
    if price > 999:
        discount = price * 0.10
        final_price = price - discount
    else:
        final_price = price
    print("you have to pay:", final_price, "bath")