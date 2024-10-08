import pytest
from q_1787_makeTheXorOfAllSegmentsEqualToZero import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [
        ([1, 2, 0, 3, 0], 1, 3),
        ([3, 4, 5, 2, 1, 7, 3, 4, 7], 3, 3),
        ([1, 2, 4, 1, 2, 5, 1, 2, 6], 3, 3),
    ],
)
class TestSolution:
    def test_minChanges(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.minChanges(
                nums,
                k,
            )
            == output
        )
