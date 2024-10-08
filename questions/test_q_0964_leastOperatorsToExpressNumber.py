import pytest
from q_0964_leastOperatorsToExpressNumber import Solution


@pytest.mark.parametrize(
    "x, target, output", [(3, 19, 5), (5, 501, 8), (100, 100000000, 3)]
)
class TestSolution:
    def test_leastOpsExpressTarget(self, x: int, target: int, output: int):
        sc = Solution()
        assert (
            sc.leastOpsExpressTarget(
                x,
                target,
            )
            == output
        )
