from transaction import Transaction
from processor import calculate_balance

def test_calculate_balance():
    transactions = {
        Transaction("Salary", 30000),
        Transaction("Rent", -10000),
        Transaction("Coffee", -50)
    }

    result = calculate_balance(transactions)

    assert result == 19950