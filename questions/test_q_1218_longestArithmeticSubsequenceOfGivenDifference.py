import pytest
from q_1218_longestArithmeticSubsequenceOfGivenDifference import Solution


@pytest.mark.parametrize(
    "arr, difference, output",
    [([1, 2, 3, 4], 1, 4), ([1, 3, 5, 7], 1, 1), ([1, 5, 7, 8, 5, 3, 4, 2, 1], -2, 4)],
)
class TestSolution:
    def test_longestSubsequence(self, arr: List[int], difference: int, output: int):
        sc = Solution()
        assert (
            sc.longestSubsequence(
                arr,
                difference,
            )
            == output
        )
