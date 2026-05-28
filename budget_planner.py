class BudgetTracker:
    def __init__(self):
        self.limit = 0.0
        self.spent = 0.0
    
    def set_budget(self, amount):
        self.limit = float(amount)
    
    def spend(self, amount):
        self.spent += float(amount)
    
    def get_remaining(self):
        return self.limit - self.spent