import pytest
from q_0940_distinctSubsequencesIi import Solution


@pytest.mark.parametrize("s, output", [("abc", 7), ("aba", 6), ("aaa", 3)])
class TestSolution:
    def test_distinctSubseqII(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.distinctSubseqII(
                s,
            )
            == output
        )
