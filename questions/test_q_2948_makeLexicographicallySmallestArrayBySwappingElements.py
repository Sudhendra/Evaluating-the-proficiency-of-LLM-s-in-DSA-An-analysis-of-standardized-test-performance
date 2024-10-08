import pytest
from q_2948_makeLexicographicallySmallestArrayBySwappingElements import Solution


@pytest.mark.parametrize(
    "nums, limit, output",
    [
        ([1, 5, 3, 9, 8], 2, [1, 3, 5, 8, 9]),
        ([1, 7, 6, 18, 2, 1], 3, [1, 6, 7, 18, 1, 2]),
        ([1, 7, 28, 19, 10], 3, [1, 7, 28, 19, 10]),
    ],
)
class TestSolution:
    def test_lexicographicallySmallestArray(
        self, nums: List[int], limit: int, output: List[int]
    ):
        sc = Solution()
        assert (
            sc.lexicographicallySmallestArray(
                nums,
                limit,
            )
            == output
        )
