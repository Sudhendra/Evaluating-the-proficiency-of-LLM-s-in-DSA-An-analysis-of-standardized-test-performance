import pytest
from q_1420_buildArrayWhereYouCanFindTheMaximumExactlyKComparisons import Solution


@pytest.mark.parametrize("n, m, k, output", [(2, 3, 1, 6), (5, 2, 3, 0), (9, 1, 1, 1)])
class TestSolution:
    def test_numOfArrays(self, n: int, m: int, k: int, output: int):
        sc = Solution()
        assert (
            sc.numOfArrays(
                n,
                m,
                k,
            )
            == output
        )
