import pytest
from q_2289_stepsToMakeArrayNonDecreasing import Solution


@pytest.mark.parametrize(
    "nums, output", [([5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11], 3), ([4, 5, 7, 7, 13], 0)]
)
class TestSolution:
    def test_totalSteps(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.totalSteps(
                nums,
            )
            == output
        )
