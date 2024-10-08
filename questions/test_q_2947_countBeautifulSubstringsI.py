import pytest
from q_2947_countBeautifulSubstringsI import Solution


@pytest.mark.parametrize(
    "s, k, output", [("baeyh", 2, 2), ("abba", 1, 3), ("bcdf", 1, 0)]
)
class TestSolution:
    def test_beautifulSubstrings(self, s: str, k: int, output: int):
        sc = Solution()
        assert (
            sc.beautifulSubstrings(
                s,
                k,
            )
            == output
        )
