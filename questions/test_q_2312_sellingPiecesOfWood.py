import pytest
from q_2312_sellingPiecesOfWood import Solution


@pytest.mark.parametrize(
    "m, n, prices, output",
    [
        (3, 5, [[1, 4, 2], [2, 2, 7], [2, 1, 3]], 19),
        (4, 6, [[3, 2, 10], [1, 4, 2], [4, 1, 3]], 32),
    ],
)
class TestSolution:
    def test_sellingWood(self, m: int, n: int, prices: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.sellingWood(
                m,
                n,
                prices,
            )
            == output
        )
