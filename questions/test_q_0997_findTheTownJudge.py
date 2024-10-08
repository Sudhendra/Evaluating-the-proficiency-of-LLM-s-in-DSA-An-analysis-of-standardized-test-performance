import pytest
from q_0997_findTheTownJudge import Solution


@pytest.mark.parametrize(
    "n, trust, output",
    [(2, [[1, 2]], 2), (3, [[1, 3], [2, 3]], 3), (3, [[1, 3], [2, 3], [3, 1]], -1)],
)
class TestSolution:
    def test_findJudge(self, n: int, trust: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.findJudge(
                n,
                trust,
            )
            == output
        )
