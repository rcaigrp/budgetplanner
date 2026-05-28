# BudgetPlanner

A Python module for tracking monthly income and expenses against a set limit.

## Installation / Setup

No installation required. Ensure you have Python 3 installed.

## Usage

```python
from budget_planner import BudgetTracker

# Initialize
tracker = BudgetTracker()

# Set monthly limit
tracker.set_budget(2000)

# Record expense
tracker.spend(500)

# Check remaining
print(tracker.get_remaining())
```

## Configuration

No configuration required. Data is stored in memory (or simple list for this MVP).
