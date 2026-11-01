"""
loger.py - Transaction logging decorator.
Provides the @log_transaction decorator, used to record
runtime execution details for functions across the project
(e.g. inventory updates, cart actions, checkout).

Author: Nahim
"""
# loggger.py
# Program Scope: Decorator-based transaction logging
# Logger module

from datetime import datetime
transaction_log = []
def log_transaction(func):
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Starting transaction")
        result = func(*args, **kwargs)
        print("Transaction closed")
        print(f"[{timestamp}] Transaction: {func.__name__} executed")
        transaction_log.append((func.__name__, timestamp))
        return result
    return wrapper

def summary():
    print(f"\nTotal transaction logged: {len(transaction_log)}")
    for name, time in transaction_log:
        print(f"- {name} at {time}")