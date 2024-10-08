import pytest
from q_1763_longestNiceSubstring import Solution


@pytest.mark.parametrize("s, output", [("YazaAay", "aAa"), ("Bb", "Bb"), ("c", "")])
class TestSolution:
    def test_longestNiceSubstring(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.longestNiceSubstring(
                s,
            )
            == output
        )
