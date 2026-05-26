# Suspicious Expense Detector

A Python backend/data-processing project that reads financial transactions from a CSV file, validates and categorizes them, detects suspicious spending patterns, and generates a summary report.

This project was built to practice:
- object-oriented programming
- CSV processing
- modular architecture
- clean code principles
- logging and error handling
- backend-style data processing

---

## Features

- Reads transactions from CSV
- Validates transaction data
- Categorizes transactions automatically
- Detects suspicious expenses
- Generates a transaction summary report
- Uses modular project structure
- Includes logging and error handling

---

## Suspicious Transaction Rules

The application currently flags:
- transactions above 10,000 kr
- unknown charges

Example:
- Luxury purchases
- suspicious unknown payments

---

## Technologies Used

- Python
- CSV
- logging
- object-oriented programming (OOP)

---

## Project Structure


```text
suspicious-expense-detector/
│
├── main.py
├── transaction.py
├── csv_reader.py
├── processor.py
├── report_generator.py
├── logger_config.py
├── transactions.csv
├── requirements.txt
└── README.md
```

---

## Example CSV Input

```csv
description,amount
Salary,30000
Groceries,-650
Rent,-9500
Coffee,-55
Luxury Bag,-12000
```

---

## Example Output

```text
=== Transaction Summary ===

Total Income: 33200.0
Total Expenses: -27138.0
Balance: 6062.0

=== Categories ===

Income: 3
Housing: 1
Food: 4
Health: 1
Shopping: 2
Other: 1

=== Suspicious Transactions ===

Salary | 30000.0 | Income
Luxury Bag | -12000.0 | Shopping
Unknown Charge | -999.0 | Other
```

---

## How to Run

Close the repository:

```bash
git clone <repository-url>
```

Run the application:

```bash
python main.py
```

---

## hat I Learned

This project helped me practice:

- modular project structure
- separation of concerns
- object-oriented programming
- CSV file handling
- transaction validation
- logging and debugging
- processing structured and financial data
- generating reports from processed data
- writing maintainable Python code

---

## Future Improvements:

Potential future improvements:
- SQLite database integration
- unit testing
- configurable suspicious-transaction rules
- data visualization/dashboard
- API integration
- export to JSON