import pytest
from q_1881_maximumValueAfterInsertion import Solution


@pytest.mark.parametrize("n, x, output", [("99", 9, "999"), ("-13", 2, "-123")])
class TestSolution:
    def test_maxValue(self, n: str, x: int, output: str):
        sc = Solution()
        assert (
            sc.maxValue(
                n,
                x,
            )
            == output
        )
