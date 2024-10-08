import pytest
from q_0017_letterCombinationsOfAPhoneNumber import Solution


@pytest.mark.parametrize(
    "digits, output",
    [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("", []),
        ("2", ["a", "b", "c"]),
    ],
)
class TestSolution:
    def test_letterCombinations(self, digits: str, output: List[str]):
        sc = Solution()
        assert (
            sc.letterCombinations(
                digits,
            )
            == output
        )
