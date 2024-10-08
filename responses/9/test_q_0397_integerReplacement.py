import pytest
from q_0397_integerReplacement import Solution


@pytest.mark.parametrize("n, output", [(8, 3), (7, 4), (4, 2)])
class TestSolution:
    def test_integerReplacement(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.integerReplacement(
                n,
            )
            == output
        )
