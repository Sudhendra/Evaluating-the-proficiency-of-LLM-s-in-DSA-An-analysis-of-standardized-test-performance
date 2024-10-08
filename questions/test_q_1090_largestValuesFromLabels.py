import pytest
from q_1090_largestValuesFromLabels import Solution


@pytest.mark.parametrize(
    "values, labels, numWanted, useLimit, output",
    [
        ([5, 4, 3, 2, 1], [1, 1, 2, 2, 3], 3, 1, 9),
        ([5, 4, 3, 2, 1], [1, 3, 3, 3, 2], 3, 2, 12),
        ([9, 8, 8, 7, 6], [0, 0, 0, 1, 1], 3, 1, 16),
    ],
)
class TestSolution:
    def test_largestValsFromLabels(
        self,
        values: List[int],
        labels: List[int],
        numWanted: int,
        useLimit: int,
        output: int,
    ):
        sc = Solution()
        assert (
            sc.largestValsFromLabels(
                values,
                labels,
                numWanted,
                useLimit,
            )
            == output
        )
