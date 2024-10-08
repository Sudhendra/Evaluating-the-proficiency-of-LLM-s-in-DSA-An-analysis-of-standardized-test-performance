import pytest
from q_2163_minimumDifferenceInSumsAfterRemovalOfElements import Solution


@pytest.mark.parametrize("nums, output", [([3, 1, 2], -1), ([7, 9, 5, 8, 1, 3], 1)])
class TestSolution:
    def test_minimumDifference(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minimumDifference(
                nums,
            )
            == output
        )
