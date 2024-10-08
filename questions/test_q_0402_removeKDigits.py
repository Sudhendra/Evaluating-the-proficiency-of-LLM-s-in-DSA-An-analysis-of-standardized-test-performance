import pytest
from q_0402_removeKDigits import Solution


@pytest.mark.parametrize(
    "num, k, output", [("1432219", 3, "1219"), ("10200", 1, "200"), ("10", 2, "0")]
)
class TestSolution:
    def test_removeKdigits(self, num: str, k: int, output: str):
        sc = Solution()
        assert (
            sc.removeKdigits(
                num,
                k,
            )
            == output
        )
