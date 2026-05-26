def generate_summary_report(
        income,
        expenses,
        balance,
        suspicious_transactions,
        category_counts
):
    print("\n=== Transaction Summary ===")

    print(f"Total Income: {income}")
    print(f"Total Expenses: {expenses}")
    print(f"Balance: {balance}")

    print("\n=== Categories ===")

    for category, count in category_counts.items():
        print(f"{category}: {count}")

    print("\n=== Suspicious Transactions ===")

    if not suspicious_transactions:
        print("No suspicious transactions detected.")

    else:
        for transaction in suspicious_transactions:
            print(
                f"{transaction.description} |"
                f"{transaction.amount} |"
                f"{transaction.category}"
            )