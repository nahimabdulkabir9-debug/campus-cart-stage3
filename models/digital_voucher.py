from models.item import Item

class DigitalVoucher(Item):
    def __init__ (self, item_id, name, price):
        super().__init__(item_id, name, price, stock=float('inf'))  # Digital vouchers have unlimited stock
    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        pass  # Digital vouchers do not have a stock limit, so we override the setter to do nothing