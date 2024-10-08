import pytest
from q_0704_binarySearch import Solution


@pytest.mark.parametrize(
    "nums, target, output",
    [([-1, 0, 3, 5, 9, 12], 9, 4), ([-1, 0, 3, 5, 9, 12], 2, -1)],
)
class TestSolution:
    def test_search(self, nums: List[int], target: int, output: int):
        sc = Solution()
        assert (
            sc.search(
                nums,
                target,
            )
            == output
        )
