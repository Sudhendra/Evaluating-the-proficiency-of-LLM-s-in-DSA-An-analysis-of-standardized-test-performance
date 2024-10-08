import pytest
from q_1800_maximumAscendingSubarraySum import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([10, 20, 30, 5, 10, 50], 65),
        ([10, 20, 30, 40, 50], 150),
        ([12, 17, 15, 13, 10, 11, 12], 33),
    ],
)
class TestSolution:
    def test_maxAscendingSum(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxAscendingSum(
                nums,
            )
            == output
        )
