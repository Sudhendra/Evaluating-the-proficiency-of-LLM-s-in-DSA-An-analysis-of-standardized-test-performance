import pytest
from q_0532_kDiffPairsInAnArray import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [([3, 1, 4, 1, 5], 2, 2), ([1, 2, 3, 4, 5], 1, 4), ([1, 3, 1, 5, 4], 0, 1)],
)
class TestSolution:
    def test_findPairs(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.findPairs(
                nums,
                k,
            )
            == output
        )
