import pytest
from q_2571_minimumOperationsToReduceAnIntegerTo0 import Solution


@pytest.mark.parametrize("n, output", [(39, 3), (54, 3)])
class TestSolution:
    def test_minOperations(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.minOperations(
                n,
            )
            == output
        )
