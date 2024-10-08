import pytest
from q_3068_findTheMaximumSumOfNodeValues import Solution


@pytest.mark.parametrize(
    "nums, k, edges, output",
    [
        ([1, 2, 1], 3, [[0, 1], [0, 2]], 6),
        ([2, 3], 7, [[0, 1]], 9),
        ([7, 7, 7, 7, 7, 7], 3, [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]], 42),
    ],
)
class TestSolution:
    def test_maximumValueSum(
        self, nums: List[int], k: int, edges: List[List[int]], output: int
    ):
        sc = Solution()
        assert (
            sc.maximumValueSum(
                nums,
                k,
                edges,
            )
            == output
        )
