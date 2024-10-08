import pytest
from q_3020_findTheMaximumNumberOfElementsInSubset import Solution


@pytest.mark.parametrize("nums, output", [([5, 4, 1, 2, 2], 3), ([1, 3, 2, 4], 1)])
class TestSolution:
    def test_maximumLength(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maximumLength(
                nums,
            )
            == output
        )
