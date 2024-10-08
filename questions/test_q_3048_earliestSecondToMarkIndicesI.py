import pytest
from q_3048_earliestSecondToMarkIndicesI import Solution


@pytest.mark.parametrize(
    "nums, changeIndices, output",
    [
        ([2, 2, 0], [2, 2, 2, 2, 3, 2, 2, 1], 8),
        ([1, 3], [1, 1, 1, 2, 1, 1, 1], 6),
        ([0, 1], [2, 2, 2], -1),
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
