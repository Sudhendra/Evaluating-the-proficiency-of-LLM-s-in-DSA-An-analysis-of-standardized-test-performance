import pytest
from q_1009_complementOfBase10Integer import Solution


@pytest.mark.parametrize("n, output", [(5, 2), (7, 0), (10, 5)])
class TestSolution:
    def test_bitwiseComplement(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.bitwiseComplement(
                n,
            )
            == output
        )
