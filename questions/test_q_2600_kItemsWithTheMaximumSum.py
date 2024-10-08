import pytest
from q_2600_kItemsWithTheMaximumSum import Solution


@pytest.mark.parametrize(
    "numOnes, numZeros, numNegOnes, k, output", [(3, 2, 0, 2, 2), (3, 2, 0, 4, 3)]
)
class TestSolution:
    def test_kItemsWithMaximumSum(
        self, numOnes: int, numZeros: int, numNegOnes: int, k: int, output: int
    ):
        sc = Solution()
        assert (
            sc.kItemsWithMaximumSum(
                numOnes,
                numZeros,
                numNegOnes,
                k,
            )
            == output
        )
