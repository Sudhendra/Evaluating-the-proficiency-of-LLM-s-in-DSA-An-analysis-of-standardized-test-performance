import pytest
from q_1417_reformatTheString import Solution


@pytest.mark.parametrize(
    "s, output", [("a0b1c2", "0a1b2c"), ("leetcode", ""), ("1229857369", "")]
)
class TestSolution:
    def test_reformat(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.reformat(
                s,
            )
            == output
        )
