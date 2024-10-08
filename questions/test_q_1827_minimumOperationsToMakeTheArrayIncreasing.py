import pytest
from q_1827_minimumOperationsToMakeTheArrayIncreasing import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 1, 1], 3), ([1, 5, 2, 4, 1], 14), ([8], 0)]
)
class TestSolution:
    def test_minOperations(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minOperations(
                nums,
            )
            == output
        )
