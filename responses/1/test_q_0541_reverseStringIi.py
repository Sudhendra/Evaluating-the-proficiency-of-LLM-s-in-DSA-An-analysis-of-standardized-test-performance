import pytest
from q_0541_reverseStringIi import Solution


@pytest.mark.parametrize(
    "s, k, output", [("abcdefg", 2, "bacdfeg"), ("abcd", 2, "bacd")]
)
class TestSolution:
    def test_reverseStr(self, s: str, k: int, output: str):
        sc = Solution()
        assert (
            sc.reverseStr(
                s,
                k,
            )
            == output
        )
