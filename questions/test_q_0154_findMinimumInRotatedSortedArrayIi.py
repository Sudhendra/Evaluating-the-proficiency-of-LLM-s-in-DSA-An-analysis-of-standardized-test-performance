import pytest
from q_0154_findMinimumInRotatedSortedArrayIi import Solution


@pytest.mark.parametrize("nums, output", [([1, 3, 5], 1), ([2, 2, 2, 0, 1], 0)])
class TestSolution:
    def test_findMin(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.findMin(
                nums,
            )
            == output
        )
