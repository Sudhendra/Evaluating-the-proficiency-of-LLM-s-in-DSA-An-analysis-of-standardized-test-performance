import pytest
from q_1358_numberOfSubstringsContainingAllThreeCharacters import Solution


@pytest.mark.parametrize("s, output", [("abcabc", 10), ("aaacb", 3), ("abc", 1)])
class TestSolution:
    def test_numberOfSubstrings(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.numberOfSubstrings(
                s,
            )
            == output
        )
