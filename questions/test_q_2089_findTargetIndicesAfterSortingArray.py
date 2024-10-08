import pytest
from q_2089_findTargetIndicesAfterSortingArray import Solution


@pytest.mark.parametrize(
    "nums, target, output",
    [
        ([1, 2, 5, 2, 3], 2, [1, 2]),
        ([1, 2, 5, 2, 3], 3, [3]),
        ([1, 2, 5, 2, 3], 5, [4]),
    ],
)
class TestSolution:
    def test_targetIndices(self, nums: List[int], target: int, output: List[int]):
        sc = Solution()
        assert (
            sc.targetIndices(
                nums,
                target,
            )
            == output
        )
