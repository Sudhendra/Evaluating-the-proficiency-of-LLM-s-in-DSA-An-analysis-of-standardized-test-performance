import pytest
from q_2413_smallestEvenMultiple import Solution


@pytest.mark.parametrize("n, output", [(5, 10), (6, 6)])
class TestSolution:
    def test_smallestEvenMultiple(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.smallestEvenMultiple(
                n,
            )
            == output
        )
