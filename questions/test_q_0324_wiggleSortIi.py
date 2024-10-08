import pytest
from q_0324_wiggleSortIi import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([1, 5, 1, 1, 6, 4], [1, 6, 1, 5, 1, 4]),
        ([1, 3, 2, 2, 3, 1], [2, 3, 1, 3, 1, 2]),
    ],
)
class TestSolution:
    def test_wiggleSort(self, nums: List[int], output: None):
        sc = Solution()
        assert (
            sc.wiggleSort(
                nums,
            )
            == output
        )
