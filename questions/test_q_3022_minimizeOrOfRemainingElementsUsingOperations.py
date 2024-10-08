import pytest
from q_3022_minimizeOrOfRemainingElementsUsingOperations import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [
        ([3, 5, 3, 2, 7], 2, 3),
        ([7, 3, 15, 14, 2, 8], 4, 2),
        ([10, 7, 10, 3, 9, 14, 9, 4], 1, 15),
    ],
)
class TestSolution:
    def test_minOrAfterOperations(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.minOrAfterOperations(
                nums,
                k,
            )
            == output
        )
