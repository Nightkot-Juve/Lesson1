price = 100
discount = 5
def discounted(price, discount):
    price_with_discount = price - (price * discount / 100)
    print(price_with_discount)