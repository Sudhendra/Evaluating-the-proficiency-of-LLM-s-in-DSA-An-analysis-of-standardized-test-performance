import pytest
from q_1040_movingStonesUntilConsecutiveIi import Solution


@pytest.mark.parametrize(
    "stones, output", [([7, 4, 9], [1, 2]), ([6, 5, 4, 3, 10], [2, 3])]
)
class TestSolution:
    def test_numMovesStonesII(self, stones: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.numMovesStonesII(
                stones,
            )
            == output
        )
