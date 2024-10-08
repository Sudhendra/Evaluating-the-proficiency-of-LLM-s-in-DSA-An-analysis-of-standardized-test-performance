import pytest
from q_3011_findIfArrayCanBeSorted import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([8, 4, 2, 30, 15], True), ([1, 2, 3, 4, 5], True), ([3, 16, 8, 4, 2], False)],
)
class TestSolution:
    def test_canSortArray(self, nums: List[int], output: bool):
        sc = Solution()
        assert (
            sc.canSortArray(
                nums,
            )
            == output
        )
