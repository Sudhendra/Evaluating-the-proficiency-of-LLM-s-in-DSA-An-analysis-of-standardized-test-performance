import pytest
from q_1707_maximumXorWithAnElementFromArray import Solution


@pytest.mark.parametrize(
    "nums, queries, output",
    [
        ([0, 1, 2, 3, 4], [[3, 1], [1, 3], [5, 6]], [3, 3, 7]),
        ([5, 2, 4, 6, 6, 3], [[12, 4], [8, 1], [6, 3]], [15, -1, 5]),
    ],
)
class TestSolution:
    def test_maximizeXor(
        self, nums: List[int], queries: List[List[int]], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.maximizeXor(
                nums,
                queries,
            )
            == output
        )
