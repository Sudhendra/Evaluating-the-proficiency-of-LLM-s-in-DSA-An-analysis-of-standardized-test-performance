import pytest
from q_0415_addStrings import Solution


@pytest.mark.parametrize(
    "num1, num2, output", [("11", "123", "134"), ("456", "77", "533"), ("0", "0", "0")]
)
class TestSolution:
    def test_addStrings(self, num1: str, num2: str, output: str):
        sc = Solution()
        assert (
            sc.addStrings(
                num1,
                num2,
            )
            == output
        )
