class BudgetTracker:
    def __init__(self):
        self.limit = None
        self.expenses = []

    def set_budget(self, limit):
        self.limit = limit

    def spend(self, amount):
        self.expenses.append(amount)
        return amount

    def get_spent(self):
        return sum(self.expenses)

    def get_remaining(self):
        if self.limit is None:
            return "No limit set"
        return self.limit - self.get_spent()