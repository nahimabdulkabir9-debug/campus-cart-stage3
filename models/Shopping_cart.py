from utils.decorator import log_transaction
class Shopping_cart:
    """Manages items a customer has selected"""
    def __init__(self):
        self._items = []
    
    def add_item(self, item, quantity):
        """Add an item to the shopping cart"""
        self._items.append({"item": item, "quantity": quantity})

    def get_items(self):
        return self._items

    def calculate_total(self):
        """Calculate the total cost of items in the shopping cart"""
        total = 0
        for entry in self._items:
            total += entry["item"].price * entry["quantity"]
        return total
    @log_transaction
    def checkout(self):
        """Process the checkout of the shopping cart"""
        for product in self._items:
            product["item"].stock = product["item"].stock - product["quantity"]
        total_cost = self.calculate_total()
        self._items.clear()  # Clear the cart after checkout
        