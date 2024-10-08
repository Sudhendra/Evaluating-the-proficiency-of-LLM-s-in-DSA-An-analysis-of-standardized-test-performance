import pytest
from q_1614_maximumNestingDepthOfTheParentheses import Solution


@pytest.mark.parametrize(
    "s, output", [("(1+(2*3)+((8)/4))+1", 3), ("(1)+((2))+(((3)))", 3)]
)
class TestSolution:
    def test_maxDepth(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.maxDepth(
                s,
            )
            == output
        )
