import pytest
from q_2213_longestSubstringOfOneRepeatingCharacter import Solution


@pytest.mark.parametrize(
    "s, queryCharacters, queryIndices, output",
    [("babacc", "bcb", [1, 3, 3], [3, 3, 4]), ("abyzz", "aa", [2, 1], [2, 3])],
)
class TestSolution:
    def test_longestRepeating(
        self, s: str, queryCharacters: str, queryIndices: List[int], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.longestRepeating(
                s,
                queryCharacters,
                queryIndices,
            )
            == output
        )
