import pytest
from q_1477_findTwoNonOverlappingSubArraysEachWithTargetSum import Solution


@pytest.mark.parametrize(
    "arr, target, output",
    [([3, 2, 2, 4, 3], 3, 2), ([7, 3, 4, 7], 7, 2), ([4, 3, 2, 6, 2, 3, 4], 6, -1)],
)
class TestSolution:
    def test_minSumOfLengths(self, arr: List[int], target: int, output: int):
        sc = Solution()
        assert (
            sc.minSumOfLengths(
                arr,
                target,
            )
            == output
        )
