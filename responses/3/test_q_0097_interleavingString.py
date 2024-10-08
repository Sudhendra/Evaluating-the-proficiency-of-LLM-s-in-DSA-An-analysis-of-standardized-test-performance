import pytest
from q_0097_interleavingString import Solution


@pytest.mark.parametrize(
    "s1, s2, s3, output",
    [
        ("aabcc", "dbbca", "aadbbcbcac", True),
        ("aabcc", "dbbca", "aadbbbaccc", False),
        ("", "", "", True),
    ],
)
class TestSolution:
    def test_isInterleave(self, s1: str, s2: str, s3: str, output: bool):
        sc = Solution()
        assert (
            sc.isInterleave(
                s1,
                s2,
                s3,
            )
            == output
        )
