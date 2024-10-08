import pytest
from q_1640_checkArrayFormationThroughConcatenation import Solution


@pytest.mark.parametrize(
    "arr, pieces, output",
    [
        ([15, 88], [[88], [15]], True),
        ([49, 18, 16], [[16, 18, 49]], False),
        ([91, 4, 64, 78], [[78], [4, 64], [91]], True),
    ],
)
class TestSolution:
    def test_canFormArray(self, arr: List[int], pieces: List[List[int]], output: bool):
        sc = Solution()
        assert (
            sc.canFormArray(
                arr,
                pieces,
            )
            == output
        )
