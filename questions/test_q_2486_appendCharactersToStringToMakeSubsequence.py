import pytest
from q_2486_appendCharactersToStringToMakeSubsequence import Solution


@pytest.mark.parametrize(
    "s, t, output", [("coaching", "coding", 4), ("abcde", "a", 0), ("z", "abcde", 5)]
)
class TestSolution:
    def test_appendCharacters(self, s: str, t: str, output: int):
        sc = Solution()
        assert (
            sc.appendCharacters(
                s,
                t,
            )
            == output
        )
