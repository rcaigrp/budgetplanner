class BudgetTracker:
    def __init__(self):
        self.limit = 0.0
        self.spent = 0.0

    def set_budget(self, amount):
        self.limit = amount

    def spend(self, amount):
        self.spent += amount

    def get_remaining(self):
        return self.limit - self.spent
