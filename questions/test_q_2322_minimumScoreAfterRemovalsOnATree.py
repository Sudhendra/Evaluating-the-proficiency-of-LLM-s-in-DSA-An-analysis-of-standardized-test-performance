import pytest
from q_2322_minimumScoreAfterRemovalsOnATree import Solution


@pytest.mark.parametrize(
    "nums, edges, output",
    [
        ([1, 5, 5, 4, 11], [[0, 1], [1, 2], [1, 3], [3, 4]], 9),
        ([5, 5, 2, 4, 4, 2], [[0, 1], [1, 2], [5, 2], [4, 3], [1, 3]], 0),
    ],
)
class TestSolution:
    def test_minimumScore(self, nums: List[int], edges: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.minimumScore(
                nums,
                edges,
            )
            == output
        )
