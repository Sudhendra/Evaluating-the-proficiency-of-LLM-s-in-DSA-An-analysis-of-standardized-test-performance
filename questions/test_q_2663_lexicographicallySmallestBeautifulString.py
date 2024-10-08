import pytest
from q_2663_lexicographicallySmallestBeautifulString import Solution


@pytest.mark.parametrize("s, k, output", [("abcz", 26, "abda"), ("dc", 4, "")])
class TestSolution:
    def test_smallestBeautifulString(self, s: str, k: int, output: str):
        sc = Solution()
        assert (
            sc.smallestBeautifulString(
                s,
                k,
            )
            == output
        )
