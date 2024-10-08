import pytest
from q_0015_3Sum import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
    ],
)
class TestSolution:
    def test_threeSum(self, nums: List[int], output: List[List[int]]):
        sc = Solution()
        assert (
            sc.threeSum(
                nums,
            )
            == output
        )
