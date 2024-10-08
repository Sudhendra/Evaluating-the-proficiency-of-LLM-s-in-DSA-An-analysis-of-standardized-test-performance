import pytest
from q_2869_minimumOperationsToCollectElements import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [([3, 1, 5, 4, 2], 2, 4), ([3, 1, 5, 4, 2], 5, 5), ([3, 2, 5, 3, 1], 3, 4)],
)
class TestSolution:
    def test_minOperations(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.minOperations(
                nums,
                k,
            )
            == output
        )
