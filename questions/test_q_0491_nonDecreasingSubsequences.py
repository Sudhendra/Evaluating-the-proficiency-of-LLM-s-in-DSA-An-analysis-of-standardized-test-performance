import pytest
from q_0491_nonDecreasingSubsequences import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        (
            [4, 6, 7, 7],
            [
                [4, 6],
                [4, 6, 7],
                [4, 6, 7, 7],
                [4, 7],
                [4, 7, 7],
                [6, 7],
                [6, 7, 7],
                [7, 7],
            ],
        ),
        ([4, 4, 3, 2, 1], [[4, 4]]),
    ],
)
class TestSolution:
    def test_findSubsequences(self, nums: List[int], output: List[List[int]]):
        sc = Solution()
        assert (
            sc.findSubsequences(
                nums,
            )
            == output
        )
