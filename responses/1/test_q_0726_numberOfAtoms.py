import pytest
from q_0726_numberOfAtoms import Solution


@pytest.mark.parametrize(
    "formula, output",
    [("H2O", "H2O"), ("Mg(OH)2", "H2MgO2"), ("K4(ON(SO3)2)2", "K4N2O14S4")],
)
class TestSolution:
    def test_countOfAtoms(self, formula: str, output: str):
        sc = Solution()
        assert (
            sc.countOfAtoms(
                formula,
            )
            == output
        )
