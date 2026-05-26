class Transaction:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount
        self.category = self.categorize_transaction()
        self.is_suspicious = self.check_if_suspicious()

    def categorize_transaction(self):
        description = self.description.lower()

        if description in ["salary", "freelance", "refund"]:
            return "Income"
        
        elif description in ["rent"]:
            return "Housing"
        
        elif description in ["groceries", "coffee"]:
            return "Food"
        
        elif description in ["gym"]:
            return "Health"
        
        elif description in ["online shopping", "luxury bag"]:
            return "Shopping"
        
        else:
            return "Other"
        

    def check_if_suspicious(self):
        if abs(self.amount) > 10000:
            return True
        
        if self.description.lower() == "unknown charge":
            return True
        
        return False