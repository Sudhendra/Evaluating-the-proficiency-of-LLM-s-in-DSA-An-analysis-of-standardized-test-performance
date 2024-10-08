import pytest
from q_0035_searchInsertPosition import Solution


@pytest.mark.parametrize(
    "nums, target, output",
    [([1, 3, 5, 6], 5, 2), ([1, 3, 5, 6], 2, 1), ([1, 3, 5, 6], 7, 4)],
)
class TestSolution:
    def test_searchInsert(self, nums: List[int], target: int, output: int):
        sc = Solution()
        assert (
            sc.searchInsert(
                nums,
                target,
            )
            == output
        )
