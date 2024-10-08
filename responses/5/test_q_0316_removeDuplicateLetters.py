import pytest
from q_0316_removeDuplicateLetters import Solution


@pytest.mark.parametrize("s, output", [("bcabc", "abc"), ("cbacdcbc", "acdb")])
class TestSolution:
    def test_removeDuplicateLetters(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.removeDuplicateLetters(
                s,
            )
            == output
        )
