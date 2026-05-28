import pytest
import budget_planner

class TestBudgetTracker:
    def test_criterion_1_import(self):
        """Test that the module can be imported."""
        assert budget_planner.BudgetTracker is not None

    def test_criterion_2_set_budget(self):
        """Test that the budget limit can be set."""
        tracker = budget_planner.BudgetTracker()
        tracker.set_budget(2000.0)
        assert tracker.limit == 2000.0

    def test_criterion_3_spend(self):
        """Test that an expenditure can be recorded."""
        tracker = budget_planner.BudgetTracker()
        tracker.set_budget(1000.0)
        tracker.spend(500.0)
        assert tracker.spent == 500.0
        assert tracker.get_remaining() == 500.0
