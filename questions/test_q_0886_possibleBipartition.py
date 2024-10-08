import pytest
from q_0886_possibleBipartition import Solution


@pytest.mark.parametrize(
    "n, dislikes, output",
    [(4, [[1, 2], [1, 3], [2, 4]], True), (3, [[1, 2], [1, 3], [2, 3]], False)],
)
class TestSolution:
    def test_possibleBipartition(self, n: int, dislikes: List[List[int]], output: bool):
        sc = Solution()
        assert (
            sc.possibleBipartition(
                n,
                dislikes,
            )
            == output
        )
