import pytest
from q_1968_arrayWithElementsNotEqualToAverageOfNeighbors import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([1, 2, 3, 4, 5], [1, 2, 4, 5, 3]), ([6, 2, 0, 9, 7], [9, 7, 6, 2, 0])],
)
class TestSolution:
    def test_rearrangeArray(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.rearrangeArray(
                nums,
            )
            == output
        )
