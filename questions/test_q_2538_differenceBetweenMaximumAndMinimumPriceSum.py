import pytest
from q_2538_differenceBetweenMaximumAndMinimumPriceSum import Solution


@pytest.mark.parametrize(
    "n, edges, price, output",
    [
        (6, [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5]], [9, 8, 7, 6, 10, 5], 24),
        (3, [[0, 1], [1, 2]], [1, 1, 1], 2),
    ],
)
class TestSolution:
    def test_maxOutput(
        self, n: int, edges: List[List[int]], price: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.maxOutput(
                n,
                edges,
                price,
            )
            == output
        )
