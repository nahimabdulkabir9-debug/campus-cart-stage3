from datetime import date
from models.item import Item

class PerishableItem(Item):
    def __init__(self, item_id, name, price, stock, expiration_date):
        super().__init__(item_id, name, price, stock)
        self.expiration_date = expiration_date

    def is_expired(self):
        if self.expiration_date < date.today():
            return True
        return False
    