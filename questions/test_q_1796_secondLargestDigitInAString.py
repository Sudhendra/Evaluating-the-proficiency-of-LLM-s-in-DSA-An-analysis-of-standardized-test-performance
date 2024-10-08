import pytest
from q_1796_secondLargestDigitInAString import Solution


@pytest.mark.parametrize("s, output", [("dfa12321afd", 2), ("abc1111", -1)])
class TestSolution:
    def test_secondHighest(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.secondHighest(
                s,
            )
            == output
        )
