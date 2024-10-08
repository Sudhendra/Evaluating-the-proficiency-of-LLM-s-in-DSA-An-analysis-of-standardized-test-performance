import pytest
from q_2997_minimumNumberOfOperationsToMakeArrayXorEqualToK import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([2, 1, 3, 4], 1, 2), ([2, 0, 2, 0], 0, 0)]
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
