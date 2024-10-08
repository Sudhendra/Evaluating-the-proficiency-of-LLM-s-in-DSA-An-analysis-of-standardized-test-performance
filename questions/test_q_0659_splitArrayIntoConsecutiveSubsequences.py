import pytest
from q_0659_splitArrayIntoConsecutiveSubsequences import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([1, 2, 3, 3, 4, 5], True),
        ([1, 2, 3, 3, 4, 4, 5, 5], True),
        ([1, 2, 3, 4, 4, 5], False),
    ],
)
class TestSolution:
    def test_isPossible(self, nums: List[int], output: bool):
        sc = Solution()
        assert (
            sc.isPossible(
                nums,
            )
            == output
        )
