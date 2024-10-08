import pytest
from q_0682_baseballGame import Solution


@pytest.mark.parametrize(
    "ops, output",
    [
        (["5", "2", "C", "D", "+"], 30),
        (["5", "-2", "4", "C", "D", "9", "+", "+"], 27),
        (["1", "C"], 0),
    ],
)
class TestSolution:
    def test_calPoints(self, operations: List[str], output: int):
        sc = Solution()
        assert (
            sc.calPoints(
                ops,
            )
            == output
        )
