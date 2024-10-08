import pytest
from q_0790_dominoAndTrominoTiling import Solution


@pytest.mark.parametrize("n, output", [(3, 5), (1, 1)])
class TestSolution:
    def test_numTilings(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.numTilings(
                n,
            )
            == output
        )
