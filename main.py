from logger_config import setup_logger
from csv_reader import read_transactions_from_csv

from processor import (
    calculate_total_income,
    calculate_total_expenses,
    calculate_balance,
    count_categories,
    get_suspicious_transactions
)

from report_generator import generate_summary_report

def main():
    setup_logger()

    transactions = read_transactions_from_csv("transactions.csv")

    income = calculate_total_income(transactions)
    expenses = calculate_total_expenses(transactions)
    balance = calculate_balance(transactions)

    suspicious_transactions = get_suspicious_transactions(transactions)

    category_counts = count_categories(transactions)

    generate_summary_report(
        income,
        expenses,
        balance,
        suspicious_transactions,
        category_counts
    )

if __name__ == "__main__":
    main()