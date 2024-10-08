import pytest
from q_2552_countIncreasingQuadruplets import Solution


@pytest.mark.parametrize("nums, output", [([1, 3, 2, 4, 5], 2), ([1, 2, 3, 4], 0)])
class TestSolution:
    def test_countQuadruplets(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.countQuadruplets(
                nums,
            )
            == output
        )
