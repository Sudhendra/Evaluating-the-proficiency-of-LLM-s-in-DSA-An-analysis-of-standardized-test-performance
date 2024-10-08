import pytest
from q_0467_uniqueSubstringsInWraparoundString import Solution


@pytest.mark.parametrize("s, output", [("a", 1), ("cac", 2), ("zab", 6)])
class TestSolution:
    def test_findSubstringInWraproundString(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.findSubstringInWraproundString(
                s,
            )
            == output
        )
