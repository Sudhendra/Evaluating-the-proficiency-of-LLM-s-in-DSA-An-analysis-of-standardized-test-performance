import pytest
from q_2945_findMaximumNonDecreasingArrayLength import Solution


@pytest.mark.parametrize(
    "nums, output", [([5, 2, 2], 1), ([1, 2, 3, 4], 4), ([4, 3, 2, 6], 3)]
)
class TestSolution:
    def test_findMaximumLength(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.findMaximumLength(
                nums,
            )
            == output
        )
