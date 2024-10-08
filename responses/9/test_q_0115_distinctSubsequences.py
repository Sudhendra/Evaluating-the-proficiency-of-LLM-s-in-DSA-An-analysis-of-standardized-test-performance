import pytest
from q_0115_distinctSubsequences import Solution


@pytest.mark.parametrize(
    "s, t, output", [("rabbbit", "rabbit", 3), ("babgbag", "bag", 5)]
)
class TestSolution:
    def test_numDistinct(self, s: str, t: str, output: int):
        sc = Solution()
        assert (
            sc.numDistinct(
                s,
                t,
            )
            == output
        )
