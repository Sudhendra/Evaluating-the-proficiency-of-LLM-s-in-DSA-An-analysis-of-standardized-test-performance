import pytest
from q_1805_numberOfDifferentIntegersInAString import Solution


@pytest.mark.parametrize(
    "word, output", [("a123bc34d8ef34", 3), ("leet1234code234", 2), ("a1b01c001", 1)]
)
class TestSolution:
    def test_numDifferentIntegers(self, word: str, output: int):
        sc = Solution()
        assert (
            sc.numDifferentIntegers(
                word,
            )
            == output
        )
