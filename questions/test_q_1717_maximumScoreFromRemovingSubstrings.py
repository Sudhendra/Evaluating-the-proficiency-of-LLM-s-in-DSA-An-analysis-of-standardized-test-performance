import pytest
from q_1717_maximumScoreFromRemovingSubstrings import Solution


@pytest.mark.parametrize(
    "s, x, y, output", [("cdbcbbaaabab", 4, 5, 19), ("aabbaaxybbaabb", 5, 4, 20)]
)
class TestSolution:
    def test_maximumGain(self, s: str, x: int, y: int, output: int):
        sc = Solution()
        assert (
            sc.maximumGain(
                s,
                x,
                y,
            )
            == output
        )
