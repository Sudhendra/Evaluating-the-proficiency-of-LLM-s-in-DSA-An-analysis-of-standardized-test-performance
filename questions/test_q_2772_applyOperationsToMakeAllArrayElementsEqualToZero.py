import pytest
from q_2772_applyOperationsToMakeAllArrayElementsEqualToZero import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([2, 2, 3, 1, 1, 0], 3, True), ([1, 3, 1, 1], 2, False)]
)
class TestSolution:
    def test_checkArray(self, nums: List[int], k: int, output: bool):
        sc = Solution()
        assert (
            sc.checkArray(
                nums,
                k,
            )
            == output
        )
