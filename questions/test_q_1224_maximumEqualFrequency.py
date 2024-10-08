import pytest
from q_1224_maximumEqualFrequency import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([2, 2, 1, 1, 5, 3, 3, 5], 7), ([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5], 13)],
)
class TestSolution:
    def test_maxEqualFreq(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxEqualFreq(
                nums,
            )
            == output
        )
