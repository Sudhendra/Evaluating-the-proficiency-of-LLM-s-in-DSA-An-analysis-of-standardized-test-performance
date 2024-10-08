import pytest
from q_1593_splitAStringIntoTheMaxNumberOfUniqueSubstrings import Solution


@pytest.mark.parametrize("s, output", [("ababccc", 5), ("aba", 2), ("aa", 1)])
class TestSolution:
    def test_maxUniqueSplit(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.maxUniqueSplit(
                s,
            )
            == output
        )
