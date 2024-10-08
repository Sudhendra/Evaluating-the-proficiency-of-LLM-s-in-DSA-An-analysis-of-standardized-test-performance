import pytest
from q_1481_leastNumberOfUniqueIntegersAfterKRemovals import Solution


@pytest.mark.parametrize(
    "arr, k, output", [([5, 5, 4], 1, 1), ([4, 3, 1, 1, 3, 3, 2], 3, 2)]
)
class TestSolution:
    def test_findLeastNumOfUniqueInts(self, arr: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.findLeastNumOfUniqueInts(
                arr,
                k,
            )
            == output
        )
