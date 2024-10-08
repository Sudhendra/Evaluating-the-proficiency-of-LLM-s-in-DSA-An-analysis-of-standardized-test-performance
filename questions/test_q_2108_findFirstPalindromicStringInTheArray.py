import pytest
from q_2108_findFirstPalindromicStringInTheArray import Solution


@pytest.mark.parametrize(
    "words, output",
    [
        (["abc", "car", "ada", "racecar", "cool"], "ada"),
        (["notapalindrome", "racecar"], "racecar"),
        (["def", "ghi"], ""),
    ],
)
class TestSolution:
    def test_firstPalindrome(self, words: List[str], output: str):
        sc = Solution()
        assert (
            sc.firstPalindrome(
                words,
            )
            == output
        )
