import pytest
from q_1611_minimumOneBitOperationsToMakeIntegersZero import Solution


@pytest.mark.parametrize("n, output", [(3, 2), (6, 4)])
class TestSolution:
    def test_minimumOneBitOperations(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.minimumOneBitOperations(
                n,
            )
            == output
        )
