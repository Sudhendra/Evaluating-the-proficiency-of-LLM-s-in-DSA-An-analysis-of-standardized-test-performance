import pytest
from q_1520_maximumNumberOfNonOverlappingSubstrings import Solution


@pytest.mark.parametrize(
    "s, output", [("adefaddaccc", ["e", "f", "ccc"]), ("abbaccd", ["d", "bb", "cc"])]
)
class TestSolution:
    def test_maxNumOfSubstrings(self, s: str, output: List[str]):
        sc = Solution()
        assert (
            sc.maxNumOfSubstrings(
                s,
            )
            == output
        )
