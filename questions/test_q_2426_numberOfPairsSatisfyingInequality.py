import pytest
from q_2426_numberOfPairsSatisfyingInequality import Solution


@pytest.mark.parametrize(
    "nums1, nums2, diff, output",
    [([3, 2, 5], [2, 2, 1], 1, 3), ([3, -1], [-2, 2], -1, 0)],
)
class TestSolution:
    def test_numberOfPairs(
        self, nums1: List[int], nums2: List[int], diff: int, output: int
    ):
        sc = Solution()
        assert (
            sc.numberOfPairs(
                nums1,
                nums2,
                diff,
            )
            == output
        )
