import pytest
from q_3038_maximumNumberOfOperationsWithTheSameScoreI import Solution


@pytest.mark.parametrize("nums, output", [([3, 2, 1, 4, 5], 2), ([3, 2, 6, 1, 4], 1)])
class TestSolution:
    def test_maxOperations(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxOperations(
                nums,
            )
            == output
        )
