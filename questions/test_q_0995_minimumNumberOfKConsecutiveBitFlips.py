import pytest
from q_0995_minimumNumberOfKConsecutiveBitFlips import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [([0, 1, 0], 1, 2), ([1, 1, 0], 2, -1), ([0, 0, 0, 1, 0, 1, 1, 0], 3, 3)],
)
class TestSolution:
    def test_minKBitFlips(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.minKBitFlips(
                nums,
                k,
            )
            == output
        )
