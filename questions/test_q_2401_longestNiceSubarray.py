import pytest
from q_2401_longestNiceSubarray import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 3, 8, 48, 10], 3), ([3, 1, 5, 11, 13], 1)]
)
class TestSolution:
    def test_longestNiceSubarray(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.longestNiceSubarray(
                nums,
            )
            == output
        )
