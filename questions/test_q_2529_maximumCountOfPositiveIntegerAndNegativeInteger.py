import pytest
from q_2529_maximumCountOfPositiveIntegerAndNegativeInteger import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([-2, -1, -1, 1, 2, 3], 3), ([-3, -2, -1, 0, 0, 1, 2], 3), ([5, 20, 66, 1314], 4)],
)
class TestSolution:
    def test_maximumCount(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maximumCount(
                nums,
            )
            == output
        )
