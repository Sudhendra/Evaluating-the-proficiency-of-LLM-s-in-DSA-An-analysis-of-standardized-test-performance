import pytest
from q_1753_maximumScoreFromRemovingStones import Solution


@pytest.mark.parametrize("a, b, c, output", [(2, 4, 6, 6), (4, 4, 6, 7), (1, 8, 8, 8)])
class TestSolution:
    def test_maximumScore(self, a: int, b: int, c: int, output: int):
        sc = Solution()
        assert (
            sc.maximumScore(
                a,
                b,
                c,
            )
            == output
        )
