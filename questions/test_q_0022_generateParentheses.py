import pytest
from q_0022_generateParentheses import Solution


@pytest.mark.parametrize(
    "n, output", [(3, ["((()))", "(()())", "(())()", "()(())", "()()()"]), (1, ["()"])]
)
class TestSolution:
    def test_generateParenthesis(self, n: int, output: List[str]):
        sc = Solution()
        assert (
            sc.generateParenthesis(
                n,
            )
            == output
        )
