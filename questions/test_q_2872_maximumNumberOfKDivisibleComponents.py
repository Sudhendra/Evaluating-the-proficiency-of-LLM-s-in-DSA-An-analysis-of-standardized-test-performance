import pytest
from q_2872_maximumNumberOfKDivisibleComponents import Solution


@pytest.mark.parametrize(
    "n, edges, values, k, output",
    [
        (5, [[0, 2], [1, 2], [1, 3], [2, 4]], [1, 8, 1, 4, 4], 6, 2),
        (
            7,
            [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]],
            [3, 0, 6, 1, 5, 2, 1],
            3,
            3,
        ),
    ],
)
class TestSolution:
    def test_maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int, output: int
    ):
        sc = Solution()
        assert (
            sc.maxKDivisibleComponents(
                n,
                edges,
                values,
                k,
            )
            == output
        )
