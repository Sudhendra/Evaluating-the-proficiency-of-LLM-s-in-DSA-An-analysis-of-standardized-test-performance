import pytest
from q_2606_findTheSubstringWithMaximumCost import Solution


@pytest.mark.parametrize(
    "s, chars, vals, output",
    [("adaa", "d", [-1000], 2), ("abc", "abc", [-1, -1, -1], 0)],
)
class TestSolution:
    def test_maximumCostSubstring(
        self, s: str, chars: str, vals: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.maximumCostSubstring(
                s,
                chars,
                vals,
            )
            == output
        )
