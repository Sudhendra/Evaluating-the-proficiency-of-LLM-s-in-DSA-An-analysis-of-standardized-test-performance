import pytest
from q_0581_shortestUnsortedContinuousSubarray import Solution


@pytest.mark.parametrize(
    "nums, output", [([2, 6, 4, 8, 10, 9, 15], 5), ([1, 2, 3, 4], 0), ([1], 0)]
)
class TestSolution:
    def test_findUnsortedSubarray(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.findUnsortedSubarray(
                nums,
            )
            == output
        )
