import pytest
from q_2903_findIndicesWithIndexAndValueDifferenceI import Solution


@pytest.mark.parametrize(
    "nums, indexDifference, valueDifference, output",
    [([5, 1, 4, 1], 2, 4, [0, 3]), ([2, 1], 0, 0, [0, 0]), ([1, 2, 3], 2, 4, [-1, -1])],
)
class TestSolution:
    def test_findIndices(
        self,
        nums: List[int],
        indexDifference: int,
        valueDifference: int,
        output: List[int],
    ):
        sc = Solution()
        assert (
            sc.findIndices(
                nums,
                indexDifference,
                valueDifference,
            )
            == output
        )
