import pytest
from q_1033_movingStonesUntilConsecutive import Solution


@pytest.mark.parametrize(
    "a, b, c, output", [(1, 2, 5, [1, 2]), (4, 3, 2, [0, 0]), (3, 5, 1, [1, 2])]
)
class TestSolution:
    def test_numMovesStones(self, a: int, b: int, c: int, output: List[int]):
        sc = Solution()
        assert (
            sc.numMovesStones(
                a,
                b,
                c,
            )
            == output
        )
