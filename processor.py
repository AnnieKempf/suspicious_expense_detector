def calculate_total_income(transactions):
    return sum(
        transaction.amount
        for transaction in transactions
        if transaction.amount > 0
    )


def calculate_total_expenses(transactions):
    return sum(
        transaction.amount
        for transaction in transactions
        if transaction.amount < 0
    )


def calculate_balance(transactions):
    return sum(
        transaction.amount
        for transaction in transactions
    )


def get_suspicious_transactions(transactions):
    return [
        transaction
        for transaction in transactions
        if transaction.is_suspicious
    ]


def count_categories(transactions):
    categories = {}

    for transaction in transactions:
        category = transaction.category

        if category not in categories:
            categories[category] = 1

        elif category in categories:
            categories[category] += 1

    return categories