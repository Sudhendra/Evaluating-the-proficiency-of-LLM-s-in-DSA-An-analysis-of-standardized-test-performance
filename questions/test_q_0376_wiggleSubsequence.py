import pytest
from q_0376_wiggleSubsequence import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([1, 7, 4, 9, 2, 5], 6),
        ([1, 17, 5, 10, 13, 15, 10, 5, 16, 8], 7),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 2),
    ],
)
class TestSolution:
    def test_wiggleMaxLength(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.wiggleMaxLength(
                nums,
            )
            == output
        )
