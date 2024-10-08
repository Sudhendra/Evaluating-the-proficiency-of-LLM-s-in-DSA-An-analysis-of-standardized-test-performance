import pytest
from q_2178_maximumSplitOfPositiveEvenIntegers import Solution


@pytest.mark.parametrize(
    "finalSum, output", [(12, [2, 4, 6]), (7, []), (28, [6, 8, 2, 12])]
)
class TestSolution:
    def test_maximumEvenSplit(self, finalSum: int, output: List[int]):
        sc = Solution()
        assert (
            sc.maximumEvenSplit(
                finalSum,
            )
            == output
        )
