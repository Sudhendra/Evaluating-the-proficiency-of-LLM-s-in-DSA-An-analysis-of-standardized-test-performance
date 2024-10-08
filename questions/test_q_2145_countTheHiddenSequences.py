import pytest
from q_2145_countTheHiddenSequences import Solution


@pytest.mark.parametrize(
    "differences, lower, upper, output",
    [([1, -3, 4], 1, 6, 2), ([3, -4, 5, 1, -2], -4, 5, 4), ([4, -7, 2], 3, 6, 0)],
)
class TestSolution:
    def test_numberOfArrays(
        self, differences: List[int], lower: int, upper: int, output: int
    ):
        sc = Solution()
        assert (
            sc.numberOfArrays(
                differences,
                lower,
                upper,
            )
            == output
        )
