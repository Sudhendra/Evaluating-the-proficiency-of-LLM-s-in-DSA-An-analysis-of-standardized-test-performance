import pytest
from q_1175_primeArrangements import Solution


@pytest.mark.parametrize("n, output", [(5, 12), (100, 682289015)])
class TestSolution:
    def test_numPrimeArrangements(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.numPrimeArrangements(
                n,
            )
            == output
        )
