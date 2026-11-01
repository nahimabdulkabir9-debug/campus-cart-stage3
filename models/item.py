class Item:
    """Represents a single product in the CampusCart catalog"""

    def __init__(self, item_id, name, price, stock):
        self.item_id = item_id
        self.name = name 
        self._price = price
        self._stock = stock

    @property
    def price(self):
        """Get the price of the item"""
        return self._price
    @price.setter
    def price(self, value):
        """Set the price of the item"""
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @property
    def stock(self):
        """Get the stock level of the item"""
        return self._stock

    @stock.setter
    def stock(self, value):
        """Set the stock level of the item"""
        if value < 0:
            raise ValueError("Stock cannot be negative")
        self._stock = value
