import pytest
from q_1111_maximumNestingDepthOfTwoValidParenthesesStrings import Solution


@pytest.mark.parametrize(
    "seq, output",
    [("(()())", [0, 1, 1, 1, 1, 0]), ("()(())()", [0, 0, 0, 1, 1, 0, 1, 1])],
)
class TestSolution:
    def test_maxDepthAfterSplit(self, seq: str, output: List[int]):
        sc = Solution()
        assert (
            sc.maxDepthAfterSplit(
                seq,
            )
            == output
        )
