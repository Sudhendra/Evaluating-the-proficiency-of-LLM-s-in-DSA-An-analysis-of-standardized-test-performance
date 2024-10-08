import pytest
from q_1247_minimumSwapsToMakeStringsEqual import Solution


@pytest.mark.parametrize(
    "s1, s2, output", [("xx", "yy", 1), ("xy", "yx", 2), ("xx", "xy", -1)]
)
class TestSolution:
    def test_minimumSwap(self, s1: str, s2: str, output: int):
        sc = Solution()
        assert (
            sc.minimumSwap(
                s1,
                s2,
            )
            == output
        )
