import pytest
from q_0480_slidingWindowMedian import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]),
        ([1, 2, 3, 4, 2, 3, 1, 4, 2], 3, [2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0]),
    ],
)
class TestSolution:
    def test_medianSlidingWindow(self, nums: List[int], k: int, output: List[float]):
        sc = Solution()
        assert (
            sc.medianSlidingWindow(
                nums,
                k,
            )
            == output
        )
