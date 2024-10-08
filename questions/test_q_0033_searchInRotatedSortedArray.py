import pytest
from q_0033_searchInRotatedSortedArray import Solution


@pytest.mark.parametrize(
    "nums, target, output",
    [([4, 5, 6, 7, 0, 1, 2], 0, 4), ([4, 5, 6, 7, 0, 1, 2], 3, -1), ([1], 0, -1)],
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
