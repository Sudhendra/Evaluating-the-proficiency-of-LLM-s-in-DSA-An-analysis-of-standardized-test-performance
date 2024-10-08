import pytest
from q_2070_mostBeautifulItemForEachQuery import Solution


@pytest.mark.parametrize(
    "items, queries, output",
    [
        (
            [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]],
            [1, 2, 3, 4, 5, 6],
            [2, 4, 5, 5, 6, 6],
        ),
        ([[1, 2], [1, 2], [1, 3], [1, 4]], [1], [4]),
        ([[10, 1000]], [5], [0]),
    ],
)
class TestSolution:
    def test_maximumBeauty(
        self, items: List[List[int]], queries: List[int], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.maximumBeauty(
                items,
                queries,
            )
            == output
        )
