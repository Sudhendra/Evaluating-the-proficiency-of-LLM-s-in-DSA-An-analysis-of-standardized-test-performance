import pytest
from q_1625_lexicographicallySmallestStringAfterApplyingOperations import Solution


@pytest.mark.parametrize(
    "s, a, b, output",
    [("5525", 9, 2, "2050"), ("74", 5, 1, "24"), ("0011", 4, 2, "0011")],
)
class TestSolution:
    def test_findLexSmallestString(self, s: str, a: int, b: int, output: str):
        sc = Solution()
        assert (
            sc.findLexSmallestString(
                s,
                a,
                b,
            )
            == output
        )
