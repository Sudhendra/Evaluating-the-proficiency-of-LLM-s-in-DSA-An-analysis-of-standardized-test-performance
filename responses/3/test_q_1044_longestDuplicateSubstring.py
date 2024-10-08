import pytest
from q_1044_longestDuplicateSubstring import Solution


@pytest.mark.parametrize("s, output", [("banana", "ana"), ("abcd", "")])
class TestSolution:
    def test_longestDupSubstring(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.longestDupSubstring(
                s,
            )
            == output
        )
