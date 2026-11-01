from models.item import Item
from models.Shopping_cart import Shopping_cart
from models.payment_methods import CashPayment

bread = Item("101", "Bread", 1500, 10)
cart = Shopping_cart()
cart.add_item(bread, 2)
cart.checkout()
payment = CashPayment()
result = payment.process_payment(3000)
print(result)

scarce = Item("102", "Drink", 800, 1)
cart2 = Shopping_cart()
cart2.add_item(scarce, 5)
try:
    cart2.checkout()
except ValueError:
    print("Error caught correctly")


print(bread.stock)