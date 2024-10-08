import pytest
from q_1155_numberOfDiceRollsWithTargetSum import Solution


@pytest.mark.parametrize(
    "n, k, target, output", [(1, 6, 3, 1), (2, 6, 7, 6), (30, 30, 500, 222616187)]
)
class TestSolution:
    def test_numRollsToTarget(self, n: int, k: int, target: int, output: int):
        sc = Solution()
        assert (
            sc.numRollsToTarget(
                n,
                k,
                target,
            )
            == output
        )
