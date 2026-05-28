import pytest
from budget_planner import BudgetTracker

def test_criterion_1_import():
    from budget_planner import BudgetTracker
    assert callable(BudgetTracker)

def test_criterion_2_set_budget():
    tracker = BudgetTracker()
    tracker.set_budget(1000)
    assert tracker.limit == 1000

def test_criterion_3_spend():
    tracker = BudgetTracker()
    tracker.set_budget(1000)
    tracker.spend(200)
    assert len(tracker.expenses) == 1
    assert tracker.expenses[0] == 200