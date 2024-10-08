import pytest
from q_0087_scrambleString import Solution


@pytest.mark.parametrize(
    "s1, s2, output",
    [("great", "rgeat", True), ("abcde", "caebd", False), ("a", "a", True)],
)
class TestSolution:
    def test_isScramble(self, s1: str, s2: str, output: bool):
        sc = Solution()
        assert (
            sc.isScramble(
                s1,
                s2,
            )
            == output
        )
