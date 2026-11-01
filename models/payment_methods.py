from models.payment import Payment
class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Cash payment of ${amount} received.")
        return {"status": "success", "method": "cash", "amount": amount}

class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"Card payment of ${amount} received.")
        return {"status": "success", "method": "card", "amount": amount}

class MobileMoneyPayment(Payment):
    def process_payment(self, amount):
            print(f"Mobile money payment of ${amount} received.")
            return {"status": "success", "method": "mobile money", "amount": amount}