import pytest
from q_1759_countNumberOfHomogenousSubstrings import Solution


@pytest.mark.parametrize("s, output", [("abbcccaa", 13), ("xy", 2), ("zzzzz", 15)])
class TestSolution:
    def test_countHomogenous(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.countHomogenous(
                s,
            )
            == output
        )
