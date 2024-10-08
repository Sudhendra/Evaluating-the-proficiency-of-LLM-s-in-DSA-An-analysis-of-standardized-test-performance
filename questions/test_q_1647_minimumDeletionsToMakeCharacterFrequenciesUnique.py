import pytest
from q_1647_minimumDeletionsToMakeCharacterFrequenciesUnique import Solution


@pytest.mark.parametrize("s, output", [("aab", 0), ("aaabbbcc", 2), ("ceabaacb", 2)])
class TestSolution:
    def test_minDeletions(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.minDeletions(
                s,
            )
            == output
        )
