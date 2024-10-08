import pytest
from q_0921_minimumAddToMakeParenthesesValid import Solution


@pytest.mark.parametrize("s, output", [("())", 1), ("(((", 3)])
class TestSolution:
    def test_minAddToMakeValid(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.minAddToMakeValid(
                s,
            )
            == output
        )
