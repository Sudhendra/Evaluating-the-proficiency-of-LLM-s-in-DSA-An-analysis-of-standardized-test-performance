import pytest
from q_2318_numberOfDistinctRollSequences import Solution


@pytest.mark.parametrize("n, output", [(4, 184), (2, 22)])
class TestSolution:
    def test_distinctSequences(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.distinctSequences(
                n,
            )
            == output
        )
