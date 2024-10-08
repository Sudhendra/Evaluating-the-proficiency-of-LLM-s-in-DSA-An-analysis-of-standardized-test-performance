import pytest
from q_0952_largestComponentSizeByCommonFactor import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([4, 6, 15, 35], 4), ([20, 50, 9, 63], 2), ([2, 3, 6, 7, 4, 12, 21, 39], 8)],
)
class TestSolution:
    def test_largestComponentSize(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.largestComponentSize(
                nums,
            )
            == output
        )
