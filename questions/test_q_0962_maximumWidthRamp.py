import pytest
from q_0962_maximumWidthRamp import Solution


@pytest.mark.parametrize(
    "nums, output", [([6, 0, 8, 2, 1, 5], 4), ([9, 8, 1, 0, 1, 9, 4, 0, 4, 1], 7)]
)
class TestSolution:
    def test_maxWidthRamp(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxWidthRamp(
                nums,
            )
            == output
        )
