import pytest
from q_0377_combinationSumIv import Solution


@pytest.mark.parametrize("nums, target, output", [([1, 2, 3], 4, 7), ([9], 3, 0)])
class TestSolution:
    def test_combinationSum4(self, nums: List[int], target: int, output: int):
        sc = Solution()
        assert (
            sc.combinationSum4(
                nums,
                target,
            )
            == output
        )
