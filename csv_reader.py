import logging
import csv
from transaction import Transaction

def read_transactions_from_csv(filename):
    transactions = []

    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                description = row.get("description")
                amount = row.get("amount")

                if not description or not amount:
                    logging.warning(f"Skipping invalid row: {row}")
                    continue

                try:
                    amount = float(amount)
                except ValueError:
                    logging.warning(f"Skipping row with invalid amount: {row}")
                    continue

                transaction = Transaction(description, amount)
                transactions.append(transaction)

        logging.info(f"Read {len(transactions)} transactions from {filename}")
        return transactions
    
    except FileNotFoundError:
        logging.error(f"File not found: {filename}")
        raise
    