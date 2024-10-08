import pytest
from q_0081_searchInRotatedSortedArrayIi import Solution


@pytest.mark.parametrize(
    "nums, target, output",
    [([2, 5, 6, 0, 0, 1, 2], 0, True), ([2, 5, 6, 0, 0, 1, 2], 3, False)],
)
class TestSolution:
    def test_search(self, nums: List[int], target: int, output: bool):
        sc = Solution()
        assert (
            sc.search(
                nums,
                target,
            )
            == output
        )
