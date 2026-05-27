from transaction import Transaction

def test_salary_categorization():
    transaction = Transaction("Salary", 30000)

    assert transaction.category == "Income"


def test_luxury_bag_is_suspicious():
        transaction = Transaction("Luxury Bag", -12000)

        assert transaction.is_suspicious is True


def test_coffee_is_not_suspicious():
      transaction = Transaction("Coffee", -50)

      assert transaction.is_suspicious is False