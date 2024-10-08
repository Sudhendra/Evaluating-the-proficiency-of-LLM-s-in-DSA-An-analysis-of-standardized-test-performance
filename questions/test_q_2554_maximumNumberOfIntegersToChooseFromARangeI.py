import pytest
from q_2554_maximumNumberOfIntegersToChooseFromARangeI import Solution


@pytest.mark.parametrize(
    "banned, n, maxSum, output",
    [([1, 6, 5], 5, 6, 2), ([1, 2, 3, 4, 5, 6, 7], 8, 1, 0), ([11], 7, 50, 7)],
)
class TestSolution:
    def test_maxCount(self, banned: List[int], n: int, maxSum: int, output: int):
        sc = Solution()
        assert (
            sc.maxCount(
                banned,
                n,
                maxSum,
            )
            == output
        )
