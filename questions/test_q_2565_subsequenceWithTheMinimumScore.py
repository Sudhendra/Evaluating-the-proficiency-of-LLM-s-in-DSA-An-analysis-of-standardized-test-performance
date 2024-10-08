import pytest
from q_2565_subsequenceWithTheMinimumScore import Solution


@pytest.mark.parametrize("s, t, output", [("abacaba", "bzaa", 1), ("cde", "xyz", 3)])
class TestSolution:
    def test_minimumScore(self, s: str, t: str, output: int):
        sc = Solution()
        assert (
            sc.minimumScore(
                s,
                t,
            )
            == output
        )
