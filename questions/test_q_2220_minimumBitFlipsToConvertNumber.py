import pytest
from q_2220_minimumBitFlipsToConvertNumber import Solution


@pytest.mark.parametrize("start, goal, output", [(10, 7, 3), (3, 4, 3)])
class TestSolution:
    def test_minBitFlips(self, start: int, goal: int, output: int):
        sc = Solution()
        assert (
            sc.minBitFlips(
                start,
                goal,
            )
            == output
        )
