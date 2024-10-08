import pytest
from q_1737_changeMinimumCharactersToSatisfyOneOfThreeConditions import Solution


@pytest.mark.parametrize("a, b, output", [("aba", "caa", 2), ("dabadd", "cda", 3)])
class TestSolution:
    def test_minCharacters(self, a: str, b: str, output: int):
        sc = Solution()
        assert (
            sc.minCharacters(
                a,
                b,
            )
            == output
        )
