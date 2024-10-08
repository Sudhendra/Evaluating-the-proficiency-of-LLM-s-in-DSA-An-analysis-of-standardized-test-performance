import pytest
from q_0209_minimumSizeSubarraySum import Solution


@pytest.mark.parametrize(
    "target, nums, output",
    [(7, [2, 3, 1, 2, 4, 3], 2), (4, [1, 4, 4], 1), (11, [1, 1, 1, 1, 1, 1, 1, 1], 0)],
)
class TestSolution:
    def test_minSubArrayLen(self, target: int, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minSubArrayLen(
                target,
                nums,
            )
            == output
        )
