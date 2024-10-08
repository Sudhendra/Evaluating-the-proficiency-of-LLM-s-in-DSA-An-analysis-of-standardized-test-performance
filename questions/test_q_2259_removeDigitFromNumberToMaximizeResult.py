import pytest
from q_2259_removeDigitFromNumberToMaximizeResult import Solution


@pytest.mark.parametrize(
    "number, digit, output",
    [("123", "3", "12"), ("1231", "1", "231"), ("551", "5", "51")],
)
class TestSolution:
    def test_removeDigit(self, number: str, digit: str, output: str):
        sc = Solution()
        assert (
            sc.removeDigit(
                number,
                digit,
            )
            == output
        )
