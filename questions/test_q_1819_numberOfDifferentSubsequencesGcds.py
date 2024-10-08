import pytest
from q_1819_numberOfDifferentSubsequencesGcds import Solution


@pytest.mark.parametrize("nums, output", [([6, 10, 3], 5), ([5, 15, 40, 5, 6], 7)])
class TestSolution:
    def test_countDifferentSubsequenceGCDs(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.countDifferentSubsequenceGCDs(
                nums,
            )
            == output
        )
