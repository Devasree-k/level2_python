
n = int(input("Enter the no.of products :"))

product_price = []
for i in range (1,n+1):
    price = float(input(f"Enter the price of product {i} : "))
    product_price.append(price)

subtotal = sum(product_price)

if subtotal > 5000 :
    discount = 0.20
elif subtotal > 2500 : 
    discount = 0.10
else:
    discount = 0.05

discount_amount = subtotal * discount
after_discount = subtotal - discount_amount

tax_amount = after_discount * 0.05

final_amount = after_discount + tax_amount


print("\nShopping Cart Summary ")
print(f"Subtotal: {subtotal}")
print(f"Discount : {after_discount}")
print(f"Tax (5%): {tax_amount}")
print(f"Final Amount: {final_amount}")
