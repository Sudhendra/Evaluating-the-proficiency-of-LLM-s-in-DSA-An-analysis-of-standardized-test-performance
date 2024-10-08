import pytest
from q_0990_satisfiabilityOfEqualityEquations import Solution


@pytest.mark.parametrize(
    "equations, output", [(["a==b", "b!=a"], False), (["b==a", "a==b"], True)]
)
class TestSolution:
    def test_equationsPossible(self, equations: List[str], output: bool):
        sc = Solution()
        assert (
            sc.equationsPossible(
                equations,
            )
            == output
        )
