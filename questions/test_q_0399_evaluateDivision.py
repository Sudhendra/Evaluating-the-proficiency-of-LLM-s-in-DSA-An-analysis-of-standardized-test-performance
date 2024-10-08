import pytest
from q_0399_evaluateDivision import Solution


@pytest.mark.parametrize(
    "equations, values, queries, output",
    [
        (
            [["a", "b"], ["b", "c"]],
            [2.0, 3.0],
            [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
            [6.0, 0.5, -1.0, 1.0, -1.0],
        ),
        (
            [["a", "b"], ["b", "c"], ["bc", "cd"]],
            [1.5, 2.5, 5.0],
            [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
            [3.75, 0.4, 5.0, 0.2],
        ),
        (
            [["a", "b"]],
            [0.5],
            [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]],
            [0.5, 2.0, -1.0, -1.0],
        ),
    ],
)
class TestSolution:
    def test_calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]],
        output: List[float],
    ):
        sc = Solution()
        assert (
            sc.calcEquation(
                equations,
                values,
                queries,
            )
            == output
        )
