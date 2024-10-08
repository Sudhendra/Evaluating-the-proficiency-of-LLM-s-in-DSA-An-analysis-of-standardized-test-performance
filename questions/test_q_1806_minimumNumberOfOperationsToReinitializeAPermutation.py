import pytest
from q_1806_minimumNumberOfOperationsToReinitializeAPermutation import Solution


@pytest.mark.parametrize("n, output", [(2, 1), (4, 2), (6, 4)])
class TestSolution:
    def test_reinitializePermutation(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.reinitializePermutation(
                n,
            )
            == output
        )
