import pytest
from q_2811_checkIfItIsPossibleToSplitArray import Solution


@pytest.mark.parametrize(
    "nums, m, output",
    [([2, 2, 1], 4, True), ([2, 1, 3], 5, False), ([2, 3, 3, 2, 3], 6, True)],
)
class TestSolution:
    def test_canSplitArray(self, nums: List[int], m: int, output: bool):
        sc = Solution()
        assert (
            sc.canSplitArray(
                nums,
                m,
            )
            == output
        )
