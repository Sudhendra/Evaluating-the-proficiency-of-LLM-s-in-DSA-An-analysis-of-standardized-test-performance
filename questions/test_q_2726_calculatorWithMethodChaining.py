import pytest
from q_2726_calculatorWithMethodChaining import Solution


@pytest.mark.parametrize("output", [(8), (100), ("Division by zero is not allowed")])
class TestSolution:
    def test_calculatorWithMethodChaining(self, output: Any):
        sc = Solution()
        assert sc.calculatorWithMethodChaining() == output
