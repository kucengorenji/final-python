import uuid
from typing import Dict, TypedDict


class TransactionRow(TypedDict):
    price: float
    quantity: int


class Transaction:
    def __init__(self):
        self.id = uuid.uuid4()
        self.items: Dict[str, TransactionRow] = {}
    ###
    # 1. function that shows item list
    # 2. function that add item (consist name, qty, price)
    # 3. function that edit/update item name, qty, and price
    # 4. delete item
    # 5. check all transaction
    # 6. total price
    # 7. reset transaction
    # 8. print order

# make class that run transaction class


class DoTransaction:
    def __init__(self):
        self.transation = Transaction()

    def run(self):
        print("running transaction")


if __name__ == "__main__":
    run_app = DoTransaction()
    run_app.run()
