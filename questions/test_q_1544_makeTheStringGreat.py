import pytest
from q_1544_makeTheStringGreat import Solution


@pytest.mark.parametrize(
    "s, output", [("leEeetcode", "leetcode"), ("abBAcC", ""), ("s", "s")]
)
class TestSolution:
    def test_makeGood(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.makeGood(
                s,
            )
            == output
        )
