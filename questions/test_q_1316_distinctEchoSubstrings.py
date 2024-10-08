import pytest
from q_1316_distinctEchoSubstrings import Solution


@pytest.mark.parametrize("text, output", [("abcabcabc", 3), ("leetcodeleetcode", 2)])
class TestSolution:
    def test_distinctEchoSubstrings(self, text: str, output: int):
        sc = Solution()
        assert (
            sc.distinctEchoSubstrings(
                text,
            )
            == output
        )
