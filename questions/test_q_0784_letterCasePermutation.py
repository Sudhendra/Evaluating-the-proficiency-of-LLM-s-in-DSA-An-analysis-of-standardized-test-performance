import pytest
from q_0784_letterCasePermutation import Solution


@pytest.mark.parametrize(
    "s, output", [("a1b2", ["a1b2", "a1B2", "A1b2", "A1B2"]), ("3z4", ["3z4", "3Z4"])]
)
class TestSolution:
    def test_letterCasePermutation(self, s: str, output: List[str]):
        sc = Solution()
        assert (
            sc.letterCasePermutation(
                s,
            )
            == output
        )
