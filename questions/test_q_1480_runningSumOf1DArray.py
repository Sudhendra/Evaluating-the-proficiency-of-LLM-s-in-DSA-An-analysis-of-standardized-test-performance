import pytest
from q_1480_runningSumOf1DArray import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([1, 2, 3, 4], [1, 3, 6, 10]),
        ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
        ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
    ],
)
class TestSolution:
    def test_runningSum(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.runningSum(
                nums,
            )
            == output
        )
