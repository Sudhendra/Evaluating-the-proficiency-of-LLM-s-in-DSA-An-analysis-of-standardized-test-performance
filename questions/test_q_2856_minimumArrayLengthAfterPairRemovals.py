import pytest
from q_2856_minimumArrayLengthAfterPairRemovals import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 3, 4, 9], 0), ([2, 3, 6, 9], 0), ([1, 1, 2], 1)]
)
class TestSolution:
    def test_minLengthAfterRemovals(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.minLengthAfterRemovals(
                nums,
            )
            == output
        )
