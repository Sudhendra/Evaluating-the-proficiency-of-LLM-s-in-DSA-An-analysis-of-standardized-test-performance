import pytest
from q_3040_maximumNumberOfOperationsWithTheSameScoreIi import Solution


@pytest.mark.parametrize(
    "nums, output", [([3, 2, 1, 2, 3, 4], 3), ([3, 2, 6, 1, 4], 2)]
)
class TestSolution:
    def test_maxOperations(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxOperations(
                nums,
            )
            == output
        )
