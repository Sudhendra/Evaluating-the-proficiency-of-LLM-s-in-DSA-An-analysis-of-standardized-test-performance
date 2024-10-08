import pytest
from q_2055_platesBetweenCandles import Solution


@pytest.mark.parametrize(
    "s, queries, output",
    [
        ("**|**|***|", [[2, 5], [5, 9]], [2, 3]),
        (
            "***|**|*****|**||**|*",
            [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]],
            [9, 0, 0, 0, 0],
        ),
    ],
)
class TestSolution:
    def test_platesBetweenCandles(
        self, s: str, queries: List[List[int]], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.platesBetweenCandles(
                s,
                queries,
            )
            == output
        )
