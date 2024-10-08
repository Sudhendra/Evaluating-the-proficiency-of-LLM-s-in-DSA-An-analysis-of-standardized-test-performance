import pytest
from q_0239_slidingWindowMaximum import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]), ([1], 1, [1])],
)
class TestSolution:
    def test_maxSlidingWindow(self, nums: List[int], k: int, output: List[int]):
        sc = Solution()
        assert (
            sc.maxSlidingWindow(
                nums,
                k,
            )
            == output
        )
