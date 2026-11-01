import streamlit as st
from models.item import Item
from models.Shopping_cart import Shopping_cart
from models.payment_methods import CashPayment, CardPayment, MobileMoneyPayment
from datetime import date 
from models.perishable_item import PerishableItem
from models.digital_voucher import DigitalVoucher
from utils.receipt import stream_receipt_lines

st.set_page_config(layout="wide")
st.title("CampusCart")
if "message" in st.session_state:
    st.success(st.session_state.pop("message"))
if "receipt" in st.session_state:
    st.code(st.session_state.pop("receipt"))

if "catalog" not in st.session_state:
    st.session_state.catalog = [
        Item("100", "Notebook", 2.50, 15),
        Item("101", "Pen", 1, 40),
        Item("102", "Bottled Water", 2, 25),
        PerishableItem("103", "Meat Pie", 6, 12, date(2026, 11, 30)),
        DigitalVoucher("104", "Campus Wi-Fi Voucher", 4.00),
    ]
    if "cart" not in st.session_state:
        st.session_state.cart = Shopping_cart()
col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("Catalog")
    for item in st.session_state.catalog:
        st.metric(item.name, f"${item.price:.2f}")
        st.write(f"Stock: {item.stock}")
        qty = st.number_input("Quantity", min_value=1, value=1, step=1, key=f"qty_{item.item_id}")

        if st.button("Add to Cart", key=f"add_{item.item_id}"):
            if qty > item.stock:
                st.warning("Not enough stock")
            else:
                st.session_state.cart.add_item(item, qty)
                st.toast(f"Added {qty} x {item.name}")
        st.divider()
        
with col2:
    st.subheader("Cart")
    cart = st.session_state.cart

    if not cart.get_items():
        st.info("Your cart is empty")
    else:
        st.code("\n".join(stream_receipt_lines(cart.get_items())))

    total = cart.calculate_total()
    st.metric("Total", f"${total:.2f}")

    method = st.selectbox("Payment method", ["Cash", "Card", "Mobile Money"])

    if st.button("Checkout"):
        payments = {
            "Cash": CashPayment(),
            "Card": CardPayment(),
            "Mobile Money": MobileMoneyPayment(),
        }
        result = payments[method].process_payment(total)
        receipt = "\n".join(stream_receipt_lines(cart.get_items()))
        receipt += f"\nTotal: ${total:.2f}\nPaid by: {result['method']}"
        receipt += "\nThank you for shopping with CampusCart!"
        cart.checkout()
        st.session_state.receipt = receipt
        st.session_state.message = f"Sale recorded ${total:.2f} paid by {result['method']}."
        st.rerun()
