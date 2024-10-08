import pytest
from q_1829_maximumXorForEachQuery import Solution


@pytest.mark.parametrize(
    "nums, maximumBit, output",
    [
        ([0, 1, 1, 3], 2, [0, 3, 2, 3]),
        ([2, 3, 4, 7], 3, [5, 2, 6, 5]),
        ([0, 1, 2, 2, 5, 7], 3, [4, 3, 6, 4, 6, 7]),
    ],
)
class TestSolution:
    def test_getMaximumXor(self, nums: List[int], maximumBit: int, output: List[int]):
        sc = Solution()
        assert (
            sc.getMaximumXor(
                nums,
                maximumBit,
            )
            == output
        )
