import pytest
from q_1941_checkIfAllCharactersHaveEqualNumberOfOccurrences import Solution


@pytest.mark.parametrize("s, output", [("abacbc", True), ("aaabb", False)])
class TestSolution:
    def test_areOccurrencesEqual(self, s: str, output: bool):
        sc = Solution()
        assert (
            sc.areOccurrencesEqual(
                s,
            )
            == output
        )
