def stream_receipt_lines(cart_items):
    for entry in cart_items:
        yield f"{entry['item'].name} x {entry['quantity']} = ${entry['item'].price * entry['quantity']:.2f}"