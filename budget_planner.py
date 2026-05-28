class BudgetTracker:
    def __init__(self):
        self.limit = 0
        self.expenses = []

    def set_budget(self, limit):
        self.limit = limit

    def spend(self, amount):
        self.expenses.append(amount)

    def get_remaining(self):
        return self.limit - sum(self.expenses)
