import pytest
from q_2239_findClosestNumberToZero import Solution


@pytest.mark.parametrize("nums, output", [([-4, -2, 1, 4, 8], 1), ([2, -1, 1], 1)])
class TestSolution:
    def test_findClosestNumber(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.findClosestNumber(
                nums,
            )
            == output
        )
