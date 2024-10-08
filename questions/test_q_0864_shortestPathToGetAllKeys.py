import pytest
from q_0864_shortestPathToGetAllKeys import Solution


@pytest.mark.parametrize(
    "grid, output",
    [(["@.a..", "###.#", "b.A.B"], 8), (["@..aA", "..B#.", "....b"], 6), (["@Aa"], -1)],
)
class TestSolution:
    def test_shortestPathAllKeys(self, grid: List[str], output: int):
        sc = Solution()
        assert (
            sc.shortestPathAllKeys(
                grid,
            )
            == output
        )
