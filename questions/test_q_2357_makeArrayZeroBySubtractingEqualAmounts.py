import pytest
from q_2357_makeArrayZeroBySubtractingEqualAmounts import Solution


@pytest.mark.parametrize("nums, output", [([1, 5, 0, 3, 5], 3), ([0], 0)])
class TestSolution:
    def test_minimumOperations(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minimumOperations(
                nums,
            )
            == output
        )
