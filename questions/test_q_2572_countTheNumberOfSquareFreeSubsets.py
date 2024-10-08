import pytest
from q_2572_countTheNumberOfSquareFreeSubsets import Solution


@pytest.mark.parametrize("nums, output", [([3, 4, 4, 5], 3), ([1], 1)])
class TestSolution:
    def test_squareFreeSubsets(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.squareFreeSubsets(
                nums,
            )
            == output
        )
