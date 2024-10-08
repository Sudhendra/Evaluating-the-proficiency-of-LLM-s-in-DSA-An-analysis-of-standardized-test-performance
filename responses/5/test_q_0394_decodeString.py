import pytest
from q_0394_decodeString import Solution


@pytest.mark.parametrize(
    "s, output",
    [
        ("3[a]2[bc]", "aaabcbc"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
    ],
)
class TestSolution:
    def test_decodeString(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.decodeString(
                s,
            )
            == output
        )
