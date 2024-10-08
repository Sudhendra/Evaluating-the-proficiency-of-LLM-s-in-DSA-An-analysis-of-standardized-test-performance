import pytest
from q_2011_finalValueOfVariableAfterPerformingOperations import Solution


@pytest.mark.parametrize(
    "operations, output",
    [
        (["--X", "X++", "X++"], 1),
        (["++X", "++X", "X++"], 3),
        (["X++", "++X", "--X", "X--"], 0),
    ],
)
class TestSolution:
    def test_finalValueAfterOperations(self, operations: List[str], output: int):
        sc = Solution()
        assert (
            sc.finalValueAfterOperations(
                operations,
            )
            == output
        )
