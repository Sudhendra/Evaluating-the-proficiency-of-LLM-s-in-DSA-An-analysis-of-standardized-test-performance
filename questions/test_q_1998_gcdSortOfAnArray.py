import pytest
from q_1998_gcdSortOfAnArray import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([7, 21, 3], True), ([5, 2, 6, 2], False), ([10, 5, 9, 3, 15], True)],
)
class TestSolution:
    def test_gcdSort(self, nums: List[int], output: bool):
        sc = Solution()
        assert (
            sc.gcdSort(
                nums,
            )
            == output
        )
