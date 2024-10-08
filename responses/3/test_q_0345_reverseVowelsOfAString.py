import pytest
from q_0345_reverseVowelsOfAString import Solution


@pytest.mark.parametrize("s, output", [("hello", "holle"), ("leetcode", "leotcede")])
class TestSolution:
    def test_reverseVowels(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.reverseVowels(
                s,
            )
            == output
        )
