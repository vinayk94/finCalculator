import unittest
from calculator import *
# Here we would include the financial functions we wrote earlier

class TestFinancialFunctions(unittest.TestCase):

    # Tests for Future Value
    def test_future_value_typical(self):
        """Test typical case for future value calculation."""
        self.assertAlmostEqual(future_value(1000, 0.05, 10), 1628.89, places=2)

    def test_future_value_zero_rate(self):
        """Test future value calculation when the interest rate is zero."""
        self.assertEqual(future_value(1000, 0, 10), 1000)

    def test_future_value_zero_periods(self):
        """Test future value calculation when the number of periods is zero."""
        self.assertEqual(future_value(1000, 0.05, 0), 1000)

    # Tests for Present Value
    def test_present_value_typical(self):
        """Test typical case for present value calculation."""
        self.assertAlmostEqual(present_value(1628.89, 0.05, 10), 1000, places=2)

    def test_present_value_zero_rate(self):
        """Test present value calculation when the interest rate is zero."""
        self.assertEqual(present_value(1000, 0, 10), 1000)

    def test_present_value_zero_periods(self):
        """Test present value calculation when the number of periods is zero."""
        self.assertEqual(present_value(1000, 0.05, 0), 1000)

    # Tests for Payment
    def test_payment_typical(self):
        """Test typical case for payment calculation."""
        self.assertAlmostEqual(payment(1000, 0.05, 10), 129.50, places=2)

    def test_payment_zero_rate(self):
        """Test payment calculation when the interest rate is zero."""
        self.assertEqual(payment(1000, 0, 10), 100)

    def test_payment_zero_periods(self):
        """Test that payment calculation raises an error when the number of periods is zero."""
        with self.assertRaises(ZeroDivisionError):
            payment(1000, 0.05, 0)

    # Tests for Net Present Value
    def test_net_present_value_typical(self):
        """Test typical case for net present value calculation."""
        cash_flows = [-1000, 200, 200, 300, 500]
        self.assertAlmostEqual(net_present_value(0.05, cash_flows), 174.89, places=2)

    def test_net_present_value_zero_rate(self):
        """Test net present value calculation when the interest rate is zero."""
        cash_flows = [-1000, 200, 200, 300, 500]
        self.assertEqual(net_present_value(0, cash_flows), 200)

    # Tests for Internal Rate of Return
    def test_internal_rate_of_return_typical(self):
        """Test typical case for internal rate of return calculation."""
        cash_flows = [-1000, 200, 200, 300, 500]
        self.assertAlmostEqual(internal_rate_of_return(cash_flows), 0.1214, places=4)

    def test_internal_rate_of_return_no_investment(self):
        """Test that IRR calculation raises an error when there is no initial investment."""
        cash_flows = [200, 200, 300, 500]
        with self.assertRaises(ValueError):
            internal_rate_of_return(cash_flows)

    def test_internal_rate_of_return_no_cash_flows(self):
        """Test that IRR calculation raises an error when there are no cash flows."""
        cash_flows = [-1000]
        with self.assertRaises(ValueError):
            internal_rate_of_return(cash_flows)

    # ... More tests for other functions or edge cases ...

if __name__ == '__main__':
    unittest.main()
