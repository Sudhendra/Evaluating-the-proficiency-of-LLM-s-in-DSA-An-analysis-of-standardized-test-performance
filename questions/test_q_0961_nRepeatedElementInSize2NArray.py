import pytest
from q_0961_nRepeatedElementInSize2NArray import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([1, 2, 3, 3], 3), ([2, 1, 2, 5, 3, 2], 2), ([5, 1, 5, 2, 5, 3, 5, 4], 5)],
)
class TestSolution:
    def test_repeatedNTimes(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.repeatedNTimes(
                nums,
            )
            == output
        )
