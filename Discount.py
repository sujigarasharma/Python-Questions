transcend_price = int(input("Enter the price of 4GB Transcend pen drive: "))
sony_price = int(input("Enter the price of Sony Head set: "))
samsung_price = int(input("Enter the price of Samsung tablet: "))
seagate_price = int(input("Enter the price of Seagate Hardisk 1TB: "))

total_price = transcend_price + sony_price + samsung_price + seagate_price

discount = 0.12 * total_price

total_price_after_discount = total_price - discount

print("Total bill amount to pay after 12% discount: Rs.", total_price_after_discount)
