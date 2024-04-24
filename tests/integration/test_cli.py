import unittest
import subprocess

class TestCalculatorIntegration(unittest.TestCase):

    def run_calculator(self, arguments):
        """Run the calculator with the given arguments and return output."""
        process = subprocess.run(['python', 'calculator.py'] + arguments,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 text=True)
        return process.stdout, process.stderr

    def test_future_value_integration(self):
        """Integration test for future value calculation."""
        output, error = self.run_calculator(['--future-value', '--pv=1000', '--rate=0.05', '--n=10'])
        self.assertIn("Future Value:", output)
        self.assertAlmostEqual(float(output.strip().split(":")[1]), 1628.89, places=2)
        self.assertEqual(error, '')

    def test_present_value_integration(self):
        """Integration test for present value calculation."""
        output, error = self.run_calculator(['--present-value', '--fv=1628.89', '--rate=0.05', '--n=10'])
        self.assertIn("Present Value:", output)
        self.assertAlmostEqual(float(output.strip().split(":")[1]), 1000, places=2)
        self.assertEqual(error, '')

    # ... additional tests for other functions

if __name__ == '__main__':
    unittest.main()
