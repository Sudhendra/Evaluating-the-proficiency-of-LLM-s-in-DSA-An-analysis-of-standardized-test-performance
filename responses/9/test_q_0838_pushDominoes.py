import pytest
from q_0838_pushDominoes import Solution


@pytest.mark.parametrize(
    "dominoes, output", [("RR.L", "RR.L"), (".L.R...LR..L..", "LL.RR.LLRRLL..")]
)
class TestSolution:
    def test_pushDominoes(self, dominoes: str, output: str):
        sc = Solution()
        assert (
            sc.pushDominoes(
                dominoes,
            )
            == output
        )
