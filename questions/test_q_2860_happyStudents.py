import pytest
from q_2860_happyStudents import Solution


@pytest.mark.parametrize("nums, output", [([1, 1], 2), ([6, 0, 3, 3, 6, 7, 2, 7], 3)])
class TestSolution:
    def test_countWays(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.countWays(
                nums,
            )
            == output
        )
