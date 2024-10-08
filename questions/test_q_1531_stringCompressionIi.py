import pytest
from q_1531_stringCompressionIi import Solution


@pytest.mark.parametrize(
    "s, k, output", [("aaabcccd", 2, 4), ("aabbaa", 2, 2), ("aaaaaaaaaaa", 0, 3)]
)
class TestSolution:
    def test_getLengthOfOptimalCompression(self, s: str, k: int, output: int):
        sc = Solution()
        assert (
            sc.getLengthOfOptimalCompression(
                s,
                k,
            )
            == output
        )
