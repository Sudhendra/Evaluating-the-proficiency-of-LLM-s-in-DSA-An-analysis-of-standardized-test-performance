import pytest
from q_0383_ransomNote import Solution


@pytest.mark.parametrize(
    "ransomNote, magazine, output",
    [("a", "b", False), ("aa", "ab", False), ("aa", "aab", True)],
)
class TestSolution:
    def test_canConstruct(self, ransomNote: str, magazine: str, output: bool):
        sc = Solution()
        assert (
            sc.canConstruct(
                ransomNote,
                magazine,
            )
            == output
        )
