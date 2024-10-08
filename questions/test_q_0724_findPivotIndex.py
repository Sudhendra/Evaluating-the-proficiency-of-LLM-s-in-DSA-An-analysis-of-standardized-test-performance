import pytest
from q_0724_findPivotIndex import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 7, 3, 6, 5, 6], 3), ([1, 2, 3], -1), ([2, 1, -1], 0)]
)
class TestSolution:
    def test_pivotIndex(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.pivotIndex(
                nums,
            )
            == output
        )
