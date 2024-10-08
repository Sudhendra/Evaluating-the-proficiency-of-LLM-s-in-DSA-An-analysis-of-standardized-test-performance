import pytest
from q_2840_checkIfStringsCanBeMadeEqualWithOperationsIi import Solution


@pytest.mark.parametrize(
    "s1, s2, output", [("abcdba", "cabdab", True), ("abe", "bea", False)]
)
class TestSolution:
    def test_checkStrings(self, s1: str, s2: str, output: bool):
        sc = Solution()
        assert (
            sc.checkStrings(
                s1,
                s2,
            )
            == output
        )
