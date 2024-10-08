import pytest
from q_2170_minimumOperationsToMakeTheArrayAlternating import Solution


@pytest.mark.parametrize(
    "nums, output", [([3, 1, 3, 2, 4, 3], 3), ([1, 2, 2, 2, 2], 2)]
)
class TestSolution:
    def test_minimumOperations(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minimumOperations(
                nums,
            )
            == output
        )
