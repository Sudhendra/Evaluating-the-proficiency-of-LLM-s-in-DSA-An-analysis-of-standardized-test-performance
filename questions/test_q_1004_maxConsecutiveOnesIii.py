import pytest
from q_1004_maxConsecutiveOnesIii import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [
        ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6),
        ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3, 10),
    ],
)
class TestSolution:
    def test_longestOnes(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.longestOnes(
                nums,
                k,
            )
            == output
        )
