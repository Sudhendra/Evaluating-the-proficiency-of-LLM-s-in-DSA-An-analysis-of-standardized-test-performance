import pytest
from q_3049_earliestSecondToMarkIndicesIi import Solution


@pytest.mark.parametrize(
    "nums, changeIndices, output",
    [
        ([3, 2, 3], [1, 3, 2, 2, 2, 2, 3], 6),
        ([0, 0, 1, 2], [1, 2, 1, 2, 1, 2, 1, 2], 7),
        ([1, 2, 3], [1, 2, 3], -1),
    ],
)
class TestSolution:
    def test_earliestSecondToMarkIndices(
        self, nums: List[int], changeIndices: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.earliestSecondToMarkIndices(
                nums,
                changeIndices,
            )
            == output
        )
